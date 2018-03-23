'''
    -본 프로그램은 6개의 코어를 사용하는 멀티프로세싱 post 입니다
    -producer : 데이터를 읽고 가공하여 consumer에게 전달(queue)
    -consumer : producer로부터 전달받은 데이터를 db로 전송

    -( 2 producer - 1 consumer ) x 2 구조로 구현되어 있으며 총 6 + 1(메인) 프로세스가 작동합니다
    
    **주의 :
        -디렉토리를 탐색하는 부분에서 탐색하고자 하는 디렉토리가 깊이 2의 구조를 갖고있다고 가정
            -search_directory
                -dir1
                    -.csv1
                    -.csv2
                    ...
                -dir2
                .....
    

'''


import multiprocessing
import requests
import pandas as pd
import time
import datetime
import sys
import os
import json





NUM_OF_PRODUCERS = 2 
separator = '/'
tagnames = {'SET_ID' : 'setid',
                '일일주행거리(KM)' : 'dlyd',
                '누적주행거리(KM)' : 'cumd',
                'GPS보정주행거리(M)' : 'gpsd',
                '속도(km/h)' : 'spd',
                '분당회전수(r/min)' : 'rpm',
                'GPS 위도' : 'gpsla',
                'GPS 경도' : 'gpslo',
                'GPS 방위각' : 'gpsang',
                '가속도 X' : 'accx',
                '가속도 Y' : 'accy',
                '일일연료사용량(L)' : 'dlyf',
                '누적연료사용량(L)' : 'cumf',
                '단말이상상태코드' : 'stscd',
                '브레이크신호' : 'sigbrk'}


def timeTOunixtime (real_time):
    #생략 : re모듈 사용을 통해 주어진 값을 형식화 가능#

    stime = "%s/%s/%s" %(real_time[8:10], real_time[5:7], real_time[0:4])
    sec = int(real_time[11:13])*60*60 + int(real_time[14:16])*60 +int(real_time[17:19])

    unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
    unixtime = unixday + sec
    return unixtime

def split_data(path, num = NUM_OF_PRODUCERS):
    #넘겨받은 path내의 디렉토리는 디렉토리들로 이루어져있다고 가정한다 (각 디렉토리 안에 파일)
    dir_list = sorted(os.scandir(path),key=(lambda entry: entry.name))
    _len_dir_list = int(len(dir_list) / num)
    
    splits = []    

    if _len_dir_list < num :
        splits.append(dir_list)
    else :

        for i in range(num-1):
            _from = i * _len_dir_list
            _to = _from + _len_dir_list

            splits.append(dir_list[_from:_to])

        #마지막 split은 나머지 모두를 포함
        splits.append(dir_list[(num-1)*_len_dir_list:])

    return splits


def produce(queue, list_of_dirs,i):

    logsc = open('/home/teama/logsc'+str(i)+'.txt', mode = 'a')
    
    print('(DEBUG)-PRODUCER_MANGES : '+str(list_of_dirs[0])+'~'+str(list_of_dirs[-1]))
    for d in list_of_dirs:
        _path = path +separator + d.name
        list_of_files = sorted(os.scandir(_path),key=(lambda entry: entry.name))
        for f in list_of_files:
            _process_data(queue, _path + separator + f.name)        
        logsc.write(_path+'\n')    
        print(_path)
        

    queue.put(None)
    queue.put(None)
    queue.put(None)


def _process_data(queue, f_path):
    dt =  pd.read_csv(f_path,encoding='euc-kr')
    tags = list(dt)
    tags.remove('데이터수신시간')
    tags.remove('SET_ID')

    length = len(dt)

    metric = 'HanuriTN_01'
    carid = str(dt['SET_ID'][0])

    _buffer = []

    count = 0
    for i in range(0,length):

        timestamp = int(timeTOunixtime(str(dt['데이터수신시간'][i])))
        for contentname in tags:
            count += 1
            value = str(dt[contentname][i])
            dp = dict()
            dp['metric']=metric
            dp['timestamp']=timestamp
            dp['value']=value
            dp['tags']=dict()
            dp['tags']['content']=tagnames[contentname]
            dp['tags']['carid']=carid

            _buffer.append(dp)
            
            if count >= 100 :
                queue.put(_buffer)
                _buffer = []
                count = 0
    
    if len(_buffer) != 0 :
        queue.put(_buffer)
            
def consume(queue, c_no):
    #logf_dp = open('/home/jh/logf_dp'+str(c_no)+'.txt', mode = 'a')
    logf_dp = open('/home/teama/logf_dp'+str(c_no)+'.txt', mode = 'a')
    
    
    #_url = 'http://125.140.110.217:44242/api/put?details'#sync&sync_timeout=5000'
    _url = 'http://0.0.0.0:44242/api/put?'#sync&sync_timeout=5000'
    headers = {'content-type' : 'application/json' , 'connection' : 'keep-alive'}

    sess = requests.Session()

    item = None
    while True :
        item = queue.get()
        if item != None :
            try :
                response = sess.post(_url, data = json.dumps(item), headers = headers)
                time.sleep(0.005)
                
                tries = 0
                while(response.status_code > 204 ) :
                    if tries > 10:
                        print('(DEBUG)-BAD_REQUEST : NOT HANDLED')
                        logf_dp.write(str(item)+'\n')
                        break

                    time.sleep(0.05*tries)
                    response = sess.post(_url, data = json.dumps(item), headers= headers)
                    tries += 1
            except ConnectionRefusedError as e :
                    print('(DEBUG)-EXCEPTION : CONNECTION_REFUSED')
                    time.sleep(1)
            except OSError as e:
                    print(str(datetime.datetime.time(datetime.datetime.now())))
                    
             
    logf_dp.close()

if __name__ == "__main__":
    

    #1Queue 생성 - 2 producers 생성 - 1 consumer 생성
    #producer function
    #consumer function 필요

    path = '/home/tinyos/01_data_hanuritien/data/hanuritien/201406'
    #path = '/home/jh/test'
    print('(DEBUG)-READ_DATA : '+path)

    #데이터 분리 :
    #총 4개의 producer가 있으므로 처리해야할 파일 목록을 4로 나누어 처리한다
    queues = [ multiprocessing.Queue(maxsize=300) for q in range(2) ]
    print('(DEBUG)-QUEUES : '+ str(queues))

    producer_procs = []
    consumer_procs = []


    splits = split_data(path)
    _len_splits = len(splits)
    st = time.time()


    if _len_splits == 1:
        print('(DEBUG)-CREATE : 1 producers - 1 consumer')
        producer1 = multiprocessing.Process(target = produce, args = (queues[i], splits[i*2 + 0], 0))
        consumer = multiprocessing.Process(target = consume, args = (queues[i], 0))

        producer1.start()
        consumer.start()
            
        producer_procs.append(producer1)
        consumer_procs.append(consumer)

    #create
    else :
        print('(DEBUG)-CREATE : 2 producers - 5 consumer')
        producer1 = multiprocessing.Process(target = produce, args = (queues[0], splits[0],0))
        producer2 = multiprocessing.Process(target = produce, args = (queues[1], splits[1],1))
        producer_procs.append(producer1)
        producer_procs.append(producer2)

        for i in range(5):
            consumer = multiprocessing.Process(target = consume, args = (queues[i%2], i))
            consumer_procs.append(consumer)            
    

        #start
        producer1.start()
        producer2.start()


        for c in consumer_procs:
            c.start()




    for p in producer_procs:
        p.join()
    
    for c in consumer_procs:
        c.join()

    et = time.time()        
    print('(DEBUG)-MAIN_P : DONE')
    print('(DEBUG)-TIME_ELAPSED : '+(et-st))
        


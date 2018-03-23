import multiprocessing
import time
import json
import requests
import pandas as pd
import time
import datetime
import sys
import os
import errno

'''
    process1 : 큐에 있는 데이터를 전송 (소비자)
    process2 : 가공된 데이터를 큐에 입력 (생산자)
'''


separator='/'
data_queue = None

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

def timeTOunixtime(real_time):
    #생략 : re모듈 사용을 통해 주어진 값을 형식화 가능#

    stime = "%s/%s/%s" %(real_time[8:10], real_time[5:7], real_time[0:4])
    sec = int(real_time[11:13])*60*60 + int(real_time[14:16])*60 +int(real_time[17:19])

    unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
    unixtime = unixday + sec
    return unixtime


def data_processing(path):
    global data_queue

    dt =  pd.read_csv(path,encoding='euc-kr')
    tags = list(dt)
    tags.remove('데이터수신시간')
    tags.remove('SET_ID')

    length = len(dt)

    metric = 'HanuriTN_02'
    carid = str(dt['SET_ID'][0])

    _buffer = []



    for i in range(0,length):

        timestamp = int(timeTOunixtime(str(dt['데이터수신시간'][i])))
        for contentname in tags:
            value = str(dt[contentname][i])
            dp = dict()
            dp['metric']=metric
            dp['timestamp']=timestamp
            dp['value']=value
            dp['tags']=dict()
            dp['tags']['content']=tagnames[contentname]
            dp['tags']['carid']=carid

            _buffer.append(dp)

    data_queue.put(length)
    data_queue.put(_buffer)


def recursive_dir_search(addr_target_dir):
    global logf
    global data_queue

    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        logf.write(addr_target_dir)
        return

    for entry in sorted(os.scandir(addr_target_dir),key=(lambda entry: entry.name)): # entry : os.DirEntry 객체


        try:
            #entry가 디렉토리인 경우
            if entry.is_dir(follow_symlinks = True):
                #if int(entry.name[:10]) < 211:
                #    continue

                recursive_dir_search(addr_target_dir+separator+entry.name)
                logsc.write('FINISHED WRITING: '+addr_target_dir+separator+entry.name+'\n')
                print('FINISHED WRITING : '+addr_target_dir + separator + entry.name + '\n')

            #entry가 파일인 경우
            elif entry.is_file(follow_symlinks = False):
                if len(entry.name) < 5:
                    continue

                addr_entry = addr_target_dir + separator + entry.name
                if entry.name[-4:] == '.csv': #확장자 검사 : 엑셀파일 여부 확인
                    data_processing(addr_entry)
                    print('             | finished processing: '+addr_entry)

        except OSError as e:
            #permission
            if e.errno == errno.EPERM:
                print('PERMISSION ERROR')
                logf.write('PERMISSION ERROR:'+addr_target_dir+separator+entry.name+'\n')





def consume_data(path,data_queue):

    #_url = 'http://125.140.110.217:44242/api/put?'#sync&sync_timeout=5000'
    _url = 'http://0.0.0.0:44242/api/put?'#sync&sync_timeout=5000'
    headers = {'content-type': 'application/json', 'connection':'keep-alive'}
    tot = 0
    logf_dp = open('/home/teama/faillogs_dp.txt',mode='a')


    session = requests.Session()


    while True:
        length = data_queue.get()
        if length is not None:
            item = data_queue.get()
            for i in range(0,length,100):
                response = session.post(_url, data = json.dumps(item[i:i+100]), headers= headers)#json.dumps(_buffer))
                time.sleep(0.005)

                tries = 0
                while(response.status_code > 204 ) :
                    if tries > 10:
                        logf_dp.write(str(item[i:i+100])+'\n')
                        break

                    print('bad request : '+str(response.status_code))
                    time.sleep(1.2*tries)
                    response = session.post(_url, data = json.dumps(item[i:i+100]), headers= headers)#json.dumps(_buffer))
                    tries += 1
        #-if
        elif length == None :
            print('consume done')
            break




#메인프로세스는 데이터 가공
#서브프로세스는 데이터 전송 
if __name__ == "__main__" :
    #path = '/home/teama/196'
    path = '/home/tinyos/01_data_hanuritien/data/hanuritien/201406'
    data_queue = multiprocessing.Queue()



    #프로세스 생성 (소비자)
    logf= open('/home/teama/faillogs.txt',mode='a')
    logsc = open('/home/teama/succlogs.txt',mode='a')
    logf_dp = open('/home/teama/faillogs_dp.txt',mode='a')

    '''
    logf= open('/home/jh/faillogs.txt',mode='a')
    logsc = open('/home/jh/succlogs.txt',mode='a')
    '''


    consumer = multiprocessing.Process(target=consume_data,args=(path, data_queue))
    consumer.start()


    recursive_dir_search(path)

    consumer.join()
    data_queue.put(None)
    print('Done')


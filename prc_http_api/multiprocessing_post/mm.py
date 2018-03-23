
# coding: utf-8

# In[1]:


'''

'''

import multiprocessing
import os
import pandas as pd
import datetime
import json
import sys
import errno



#서버에 질의를 던져서 얻은 결과를 가공하여 다른 서버에 재전송
def __multi_dataprocessing1(data, url, query, query_tags):
    response = __QueryData(url, query, query_tags)
    
        

#파일로부터 직접 읽어서 큐로 전송 (마스터프로세스에서는 해당 큐에서 데이터를 읽어서 전송
def __multi_dataprocessing3(data_queue) :

    dt =  pd.read_csv(path,encoding='euc-kr')
    tags = list(dt)
    tags.remove('데이터수신시간')
    tags.remove('SET_ID')

    length = len(dt)

    metric = 'test_multip'
    carid = str(dt['SET_ID'][0])

    _buffer = []
    dp = dict()


    for i in range(0,length):

        timestamp = int(timeTOunixtime(str(dt['데이터수신시간'][i])))
        for contentname in tags:
            value = str(dt[contentname][i])

            dp['metric']=metric
            dp['timestamp']=timestamp
            dp['value']=value
            dp['tags']=dict()
            dp['tags']['content']=tagnames[contentname]
            dp['tags']['carid']=carid

            _buffer.append(dp)

    #for i in range(0,length,3000):
    data_queue.put(length)
    data_queue.put(_buffer)
    
    


# In[11]:


#파일을 읽어서 데이터를 가공 후 전송
def __multi_dataprocessing2(list_of_dirs):
    log_failed_dp = open('./log_failed_dp.txt',mode='a')
    
    for directory in list_of_dirs:
        __recursive_dir_search(directory, log_failed_dp)
    
    


# In[12]:


def __recursive_dir_search(addr_target_dir, log_failed_dp):

    
    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        print ('PERMISSION ERROR:' + addr_target_dir)
        return

    for entry in sorted(os.scandir(addr_target_dir),key=(lambda entry: entry.name)): # entry : os.DirEntry 객체


        try:
            #entry가 디렉토리인 경우
            if entry.is_dir(follow_symlinks = True):

                recursive_dir_search(addr_target_dir+separator+entry.name)
                print('FINISHED WRITING : '+addr_target_dir + separator + entry.name + '\n')

            #entry가 파일인 경우
            elif entry.is_file(follow_symlinks = False):
                if len(entry.name) < 5:
                    continue

                addr_entry = addr_target_dir + separator + entry.name
                if entry.name[-4:] == '.csv': #확장자 검사 : 엑셀파일 여부 확인
                    __post_data(addr_entry, log_failed_dp)
                    print('             - FINISHED WRITING : '+addr_entry)
                    #성공적으로 전송한 경우 +1

        except OSError as e:
            #permission
            if e.errno == errno.EPERM:
                print ('PERMISSION ERROR: '+ addr_target_dir +separator+entry.name+'\n')


# In[13]:


def __post_data(path, log_failed_dp):
    _url = 'http://125.140.110.217:44242/api/put?'#sync&sync_timeout=5000'
    headers = {'content-type': 'application/json'}

    metric = 'test'

    dt = pd.read_csv(path,encoding='euc-kr')
    tags = list(dt)
    tags.remove('데이터수신시간')
    tags.remove('SET_ID')

    length = len(dt)

    carid = str(dt['SET_ID'][0])
    _buffer =  []##list of dictionaries


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
            count += 1

    for i in range(0,length,50):
        response = requests.post(_url, data = json.dumps(_buffer[i:i+100]), headers= headers)#json.dumps(_buffer))
        time.sleep(0.005)

        tries = 0
        while(response.status_code > 204 ) :
            if tries > 10:
                log_failed_dp.write('BAD_REQEUST HANDLING : '+ str(_buffer[i:i+100]))
                break

            print ('BAD REQUEST : '+str(response.status_code))
            time.sleep(0.8)
            response = requests.post(_url, data = json.dumps(_buffer[i:i+100]), headers= headers)#json.dumps(_buffer))
            tries += 1



#connected_car/lib/data_processing/opentsdb/hanuritien/1st_year/work_time/multi_proc/Draft_version/HTTP_POST_request.py
def __QueryData(_url, _required, _tags):
    headers = {'content-type': 'application/json'}

    dp = OrderedDict()    # dp (Data Point)
    dp["start"] = convertTimeToEpoch(_required["start"])
    dp["end"] = convertTimeToEpoch(_required["end"])    # not exactly required

    temp = OrderedDict()
    temp["aggregator"] = _required["aggregator"]
    temp["metric"] = _required["metric"]
    temp["tags"] = _tags

    dp["queries"] = []
    dp["queries"].append(temp)

    print ("[Querying]" + json.dumps(dp, ensure_ascii=False, indent=4))
    response = requests.post(_url, data=json.dumps(dp), headers= headers)
    
    while response.status_code > 204:
        print(" [Bad Request] Query status: %s" % (response.status_code))
        print(" [Bad Request] We got bad request, Query will be restarted after 30 sec!\n")
        time.sleep(30)
        
        response = requests.post(_url, data=json.dumps(dp), headers= headers)
    
    print(" [Query finish and out]")
    return response
# In[2]:


class Multi_data_processor :
    logf = open 
    def __init__(self, num_of_process):
        self.num_of_process = num_of_process
        self.pool = multiprocessing.Pool(processes = num_of_process)
        print ('NUM OF PROCESSES :' + str(self.num_of_process))
        
        
        
    #넘겨받은 데이터셋(data)를 프로세스 갯수만큼으로 나누어 각 프로세스로 하여금 처리하도록 한다    
    #process_func는 기본적으로 decoded data, url, query를 매개변수로 받는 함수이어야 한다
    def process_data_from_received(self, data, url, query, query_tags, process_func):#=__multi_dataprocessing1):
        _total = len(data)
        _each = _total / self.num_of_process
        
        for i in self.num_of_process:
            _from = i*_each
            _to = _from + _each
            
            self.pool.apply_async(process_func, [data[_from:_to], url, query, query_tags])
                     
                                                 
        self.pool.close() #더이상의 작업이 풀에 입력되는 것 방지
        self.pool.join() #풀의 프로세스가 종료됨을 기다린다
    
    #특정 디렉토리 안의 파일들을 각 프로세스에 분배하여 디비에 전송
    #process_func는 기본적으로 디렉토리 목록을 매개변수로 받는 함수이어야 한다 
    def process_data_from_files(self, path, process_func):#=__multi_dataprocessing2):
        #디렉토리 분배
        list_of_dirs = sorted(os.scandir(path),key=(lambda entry: entry.name))
        _length = len(list_of_dirs)
        _each = _length/self.num_of_process
        
        for i in self.num_of_process:
            _from = i*_each
            _to = _from + _each
            
            self.pool.apply_async(process_func, list_of_dirs[_from:_to])
                          
                                                 
        self.pool.close() #더이상의 작업이 풀에 입력되는 것 방지
        self.pool.join() #풀의 프로세스가 종료됨을 기다린다
        

            


# In[7]:




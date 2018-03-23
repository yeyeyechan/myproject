
# coding: utf-8

# In[35]:


'''
상황 :
    -Opentsdb에 데이터가 저장되어 있다

목적 :
    -특정 내용의 데이터들의 값의 시간당 변화량을 구하여 그래프를 도출해내는 것
    
기능 :
    -Opentsdb로부터 데이터를 읽어온다
    -데이터가공 작업 :
        -데이터 구분 : 특정 타임스탬프 a,b사이 (1시간)에 있는 값들의 평균을
                     모든 시간대에 대하여 구한다
        -형태 : 해당 시간대의 타임스탬프를 대표하는 타임스탬프는 특정 시간의 정각을 기준으로 한다
        -가공된 데이터를 pandas dataframe객체에 저장한다
    -가공된 데이터를 다시 opentsdb에 새로운 metric으로 저장한다


* carid, value에 해당하는 tag는 하드코딩함*
'''



#modules
import urllib.request
import pandas as pd
import os
import json
import time
import socket
import datetime



# In[39]:


#Globals
df = None #opentsdb로부터 읽어온 데이터를 갖고있는 데이터프레임 객체
grped_df = None #groupby가 적용된 데이터를 갖고있는 데이터프레임 객체
epoch_hour = 3600
epoch_min = 60

#socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(10)


# In[40]:


#read func
def read_data():
    global df
    st_time = "2014061300" #start time
    ed_time = "2014063000" #end time

    #query문 형태로 변환
    st = "%s/%s/%s-%s:00:00" % (st_time[0:4],st_time[4:6],st_time[6:8],st_time[8:10])
    ed = "%s/%s/%s-%s:00:00" % (ed_time[0:4],ed_time[4:6],ed_time[6:8],ed_time[8:10])

    metric = 'HanuriTN_00'
    tags = '{content=rpm}'
    agg = 'sum'

    _url = 'http://0.0.0.0:44242/api/query?'

    tsdb_url = _url+'start='+st+'&end='+ed+'&m='+agg+':'+'rate:'+metric+tags

    response = urllib.request.urlopen(tsdb_url)

    data = json.loads(response.read().decode())


    #df = pd.DataFrame(data)



    metric = data[0]['metric'] #string
    content = data[0]['tags']['content'] #string
    tagv = data[0]['tags']['carid'] # tagvalue
    timestamps = list(data[0]['dps'].keys()) #list
    values = list(data[0]['dps'].values())

    columns = ['Timestamps','Values']
    dts = { 'Timestamps' : timestamps, 'Values' : values }
    df = pd.DataFrame(data=dts,columns = columns)


# In[41]:


#function for groupby
def groupby_time(df, idx, col):
    e_time = int(df[col][idx])
    htm = time.strftime('%Y%m%d%H%M',time.localtime(e_time))
    return htm


# In[42]:


#function for writing data
def write_data():
    global grped_df
    metric = 'testresult4'
    carid = 1 # ex

    rlen = len(grped_df['Values'])
    for r in range(rlen):
        ts = timeTOunixtime(grped_df['Timestamps'][r])
        v = str(grped_df['Values'][r])
        #print(type(ts))
        
        __buf = "put %s %s %s %s \n" % (metric, ts, v, 'content=rpm carid=1')
        print(__buf)
        sock.sendall(__buf.encode())

        
def timeTOunixtime (real_time):
    #생략 : re모듈 사용을 통해 주어진 값을 형식화 가능#

    stime = "%s/%s/%s" %(real_time[6:8], real_time[4:6], real_time[0:4])
    sec = int(real_time[8:10])*60*60 + int(real_time[10:12])*60 # +int(real_time[17:19])

    unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
    unixtime = unixday + sec
    return int(unixtime)

# In[43]:


if __name__ == "__main__":
#establish connection
    host = '0.0.0.0'#'125.140.110.217'
    port = 44242
    sock.connect((host,port))

#read data from opentsdb
    read_data()
#process the data
    #Group data(df)  by groupby_time function
    grped_df = df.groupby(lambda x: groupby_time(df,x,'Timestamps')).mean()
    #grped_df['Timestamps'] = grped_df.index #index as a column
    grped_df.reset_index(inplace=True)
    grped_df.columns = ['Timestamps','Values']
    
    print(grped_df)
#write back the data
    write_data()

    sock.close()
    # ? : 데이터 입출력 과정에서 generator를 사용하여 메모리를 좀 더 효휼적으로 사용할 수는 없는가


    
    # ? : 데이터 입출력 과정에서 generator를 사용하여 메모리를 좀 더 효휼적으로 사용할 수는 없는가


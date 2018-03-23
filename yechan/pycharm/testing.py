import requests
import time
import datetime
import pandas as pd
import json
import os
import copy
enc = 'euc-kr'
url = "http://0.0.0.0:4242/api/put"
url2= "http://125.140.110.217:44242/api/put"
url3="http://1.232.245.5:4242/api/put"
dirketi='/home/tinyos/01_data_hanuritien/data/hanuritien/201406/0000000001'
dir2='/usr/local/pycharm/new'
dir3='/usr/local/pycharm/0000000001-20141231.csv'
encode='euc-kr'
tagnames = {
            '일일주행거리(KM)': 'dlyd',
            '누적주행거리(KM)': 'cumd',
            'GPS보정주행거리(M)': 'gpsd',
            '속도(km/h)': 'spd',
            '분당회전수(r/min)': 'rpm',
            'GPS 위도': 'gpsla',
            'GPS 경도': 'gpslo',
            'GPS 방위각': 'gpsang',
            '가속도 X': 'accx',
            '가속도 Y': 'accy',
            '일일연료사용량(L)': 'dlyf',
            '누적연료사용량(L)': 'cumf',
            '단말이상상태코드': 'stscd',
            '브레이크신호': 'sigbrk'}

def time2unix(_time):

    if not _time== None or len(_time)==20:

        stime = "%s/%s/%s" %(_time[8:10], _time[5:7], _time[0:4])
        sec = int(_time[11:13])*60*60 + int(_time[14:16])*60 +int(_time[17:19])

        unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
        unixtime = unixday + sec
        return int(unixtime)
    else:
        return False



def floatcheck(_value):
    value = float(_value)
    if isinstance(value, float):
        return value
    else:
        return False
def find_dir(path,list):
    if 'scandir' in dir(os):
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                find_dir(entry.path,list)
            elif entry.is_file(follow_symlinks=False):
                if entry.name[-3:] == 'csv':
                    list.append(path + '/' + entry.name)
        list.sort()
        return list
def send(path, enc):
    dt = pd.read_csv(path, encoding=enc)
    tags = list(dt)
    listdic = []

    tags.remove('데이터수신시간')
    tags.remove('SET_ID')
    for i in tags:
        for j in range(len(dt)):
            if time2unix(dt['데이터수신시간'][j]) and (floatcheck(dt[i][j]) or floatcheck(dt[i][j])==0 ):
                value = {
                            "metric": "test01",
                            "timestamp": time2unix(dt['데이터수신시간'][j]),
                            "value": floatcheck(dt[i][j]),
                            "tags": {
                                "content": tagnames[i],
                                "set_id": '%03d' % dt['SET_ID'][0]
                            }
                        }

                listdic.append(value)


            else:
                continue
        length= len(listdic)
        time=0
        before=0
        term=30000
        for  k in range(0,length,term):
            if time ==0:
                push =json.dumps(listdic[0:k])
                requests.post(url,data=push)
                time+=1
                before= k
            elif k+term>length:
                push =json.dumps(listdic[k:length])
                requests.post(url,data=push)
            else:
                push=json.dumps(listdic[before:k])
                requests.post(url,data=push)
                before=k
    print('finished %s'%path[-8:-4])
if __name__ == "__main__":
            '''addlist=[]
            csv_list=find_dir(dir3,addlist)
            for dirs in csv_list:'''
            send(dir3, encode)
            print('finished ')

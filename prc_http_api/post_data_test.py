
# -*- coding: utf-8 -*-

# Modified by :  Jeonghoonkang, github.com/jeonghoonkang

import json
import requests
import pandas as pd
import time
import datetime
import sys
import os
import errno
import scandir
import csv, codecs

count=0
separator='/'
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

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    def __iter__(self):
        return self
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    def __iter__(self):
        return self

def utf_8_line(l):
    _ulist=[]
    for item in l:
        _i = item.decode('euckr').encode('utf-8')
        _ulist.append(_i)
    return _ulist

def post_data(path):
    print(' -- Using: '+path)
    _line_cnt = 0
    global count
    _url = 'http://125.140.110.217:44242/api/put?details'#sync&sync_timeout=5000'
    headers = {'content-type' : 'application/json'}
    metric = '__test__cv__file__001__'

    _r = csv.reader(open(path))
    for line in _r:
        try:
            _list = utf_8_line(line)
            print _list
            exit()
            if _line_cnt == 0 :
                continue
            _line_cnt += 1
            for item in _list:
                print item
        except (UnicodeDecodeError) as err:
           print err
           pass
        exit("...done")

#parse N-datapoints from .csv files
def post_data_(path):
    print(' -- Using: '+path)

    global count
    _url = 'http://125.140.110.217:44242/api/put?details'#sync&sync_timeout=5000'
    headers = {'content-type' : 'application/json'}

    metric = '__test__cv__file__001__'

    dt = pd.read_csv(path,encoding='euc-kr')
    print type(dt)

    tags = list(dt)
    print len(tags)

    #for member in tags:
    print tags

    exit()
    tags = tags.decode('euc-kr')
    print tags
    exit()

    tags.remove(u'데이터수신시간')
    tags.remove(u'SET_ID')

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
    for i in range(0,length,100):
        response = requests.post(_url, data = json.dumps(_buffer[i:i+100]), headers= headers)#json.dumps(_buffer))
        time.sleep(0.005)

        tries = 0
        bad_request_handled = False
        while(response.status_code > 204 ) :
            if tries > 10:
                logf_dp.write('BAD_REQEUST HANDLING : '+ str(_buffer[i:i+100]))
                break

            print('bad request : '+str(response.status_code))
            time.sleep(1.2)
            response = requests.post(_url, data = json.dumps(_buffer[i:i+100]), headers= headers)#json.dumps(_buffer))
            tries += 1



'''
def __recursive_try(rp):
    length = len(rp)

    _url = 'http://125.140.110.217:44242/api/put?details'#sync&sync_timeout=5000'
    headers = {'content-type': 'application/json'}

    __buf = []
    for i in range(length):
        __buf.append(rp[i]['datapoint'])

    for i in range(0,length,100):
        response = requests.post(_url, data = json.dumps(__buf[i:i+100]), headers= headers)#json.dumps(_buffer))

'''

def timeTOunixtime (real_time):
    #생략 : re모듈 사용을 통해 주어진 값을 형식화 가능#

    stime = "%s/%s/%s" %(real_time[8:10], real_time[5:7], real_time[0:4])
    sec = int(real_time[11:13])*60*60 + int(real_time[14:16])*60 +int(real_time[17:19])

    unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
    unixtime = unixday + sec
    return unixtime


def recursive_dir_search(addr_target_dir):
    global logf
    global total
    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        logf.write(addr_target_dir)
        return

    for entry in sorted(scandir.scandir(addr_target_dir), \
        key=(lambda entry: entry.name)): # entry : os.DirEntry 객체

        try:
            #entry가 디렉토리인 경우
            if entry.is_dir(follow_symlinks = True):
                if int(entry.name[:10]) < 397:
                    continue

                recursive_dir_search(addr_target_dir + separator + entry.name)
                logsc.write('FINISHED WRITING: '+ addr_target_dir \
                    + separator + entry.name + '\n')
                print('FINISHED WRITING : '+addr_target_dir \
                    + separator + entry.name + '\n')

            #entry가 파일인 경우
            elif entry.is_file(follow_symlinks = False):
                if len(entry.name) < 5:
                    continue

                addr_entry = addr_target_dir + separator + entry.name
                if entry.name[-4:] == '.csv': #확장자 검사 : 엑셀파일 여부 확인
                    post_data(addr_entry)
                    '''
                        review :
                        이렇게 파일마다 읽어서 post 로 DB에 입력할 수 있지만
                        파일 리스트를 다 읽어 낸후에 진행하면 좋을듯
                        파일 갯수가 매우 많은 경우...
                        전체 리스트를 알고 진행하는게 좋을것 같음
                    '''
                    print('             | finished writing : '+addr_entry)
                    #성공적으로 전송한 경우 +1

        except OSError as e:
            #permission
            if e.errno == errno.EPERM:
                print('PERMISSION ERROR')
                logf.write('PERMISSION ERROR:' + \
                    addr_target_dir + separator + entry.name + '\n')

if __name__ == "__main__":

    logf= open('./faillogs.txt',mode='a')
    logsc = open('./succlogs.txt',mode='a')
    logf_dp = open('./faillogs_dp.txt',mode='a')

    recursive_dir_search('./201409')
    #recursive_dir_search('/home/teama/testdata2')
    print('Done')
    print('Datapoints saved :' + str(count))


    logf.close()
    logsc.close()
    logf_dp.close()

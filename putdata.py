import time
import datetime
import os
import argparse
import socket
import pandas as pd
import errno
import sys

separator = os.sep
total = 0
count = 0
logf = None
d_file = None

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
    return int(unixtime)



#지정된 파일을 지정한 인코딩으로 read
#해당 파일을 형식에 맞추어 opentsdb에 전송한다
def Write_to_opts(path,enc):
    global tagnames
    global count
    global d_file

    dt = pd.read_csv(path,encoding=enc)

    #column names
    tags = list(dt)

    tags.remove('데이터수신시간')
    tags.remove('SET_ID')

    #total num of rows
    length = len(dt)

    carid = str(dt['SET_ID'][0])
    buf = []
    
    count = 0
    for i in range(length):
        timestamp = timeTOunixtime(str(dt['데이터수신시간'][i]))
        for contentname in tags:
            count += 1
            carid = str(dt['SET_ID'][i])
            value = str(dt[contentname][i])

            content = 'content='+tagnames[contentname]+' carid='+carid
            _buf = "put %s %s %s %s \n" % ('HanuriTN_00', timestamp, value, content)
            buf.append(_buf)

            if count >= 300 :
                d_file.write(_buf)
                count = 0
                buf = []
     
    d_file.write(_buf)
    print(path)
    logsc.write(path+'\n')


def recursive_dir_search(addr_target_dir):
    global logf
    global total
    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        logf.write(addr_target_dir)
        return

    for entry in sorted(os.scandir(addr_target_dir),key=(lambda entry: entry.name)): # entry : os.DirEntry 객체


        try:
            #entry가 디렉토리인 경우
            if entry.is_dir(follow_symlinks = True):
                #if int(entry.name[:10]) < 230:
                    #continue

                recursive_dir_search(addr_target_dir+separator+entry.name)
                logsc.write('FINISHED WRITING: '+addr_target_dir+separator+entry.name+'\n')
                print('FINISHED WRITING : '+addr_target_dir + separator + entry.name + '\n')

            #entry가 파일인 경우
            elif entry.is_file(follow_symlinks = False):
                if len(entry.name) < 5:
                    continue

                addr_entry = addr_target_dir + separator + entry.name
                if entry.name[-4:]== '.csv': #확장자 검사 : 엑셀파일 여부 확인
                    total += 1
                    Write_to_opts(addr_entry,'euc-kr')
                    #성공적으로 전송한 경우 +1

        except OSError as e:
            #permission
            if e.errno == errno.EPERM:
                print('PERMISSION ERROR')
                logf.write('PERMISSION ERROR:'+addr_target_dir+separator+entry.name+'\n')



if __name__ == "__main__":
    #host = '0.0.0.0'
    host = '125.140.110.217'
    port = 44242
    #addr = '/home/tinyos/01_data_hanuritien/data/hanuritien/201408'
    addr = '/home/jh/test'

    #print('CONNECTED TO '+host+':'+str(port))
    #print('FAIL LOG FILE: /home/teama/faillogs.txt')
    #print('SUCCESS LOG FILE: /home/teama/succlogs.txt')

    logf = open('/home/jh/faillogs.txt',mode='a')
    logsc = open('/home/jh/succlogs.txt',mode='a')
    d_file = open('/home/jh/data_file.txt',mode='a')
 

    if 'scandir' in dir(os):
        recursive_dir_search(addr)

    logsc.write('total:'+str(total)+' read:'+str(count))

    logf.close()
    logsc.close()
                 

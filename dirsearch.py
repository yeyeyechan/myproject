import datetime
import time
import os
import argparse
import pandas as pd
import socket

separator = os.sep
errorlog = '/home/jh' #errorlog 파일 저장 위치
total = 0
count = 0

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


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


def parse_args():
    story = 'read xlsx files in target directory, and save them to opentsdb'
    usg = 'format:python3 run.py --addr absolute_target_directory -H hostip -P port'
    hlp =   '''
            NAME
                
            SYNOPSIS
                명령어 [OPTION] [ARG]... [[OPTION] [ARG]]
            DESCRIPTION
                search all files(.xlsx) in the target directory, and send them to the designated 
                opentsdb (host:port)
                
                --addr
                    absoulte address of the target directory
                -H
                    host ip address
                -P
                    port number
                
            '''

    parser = argparse.ArgumentParser(usage=usg)
    parser.add_argument("--addr",default=None,help=u'absolute addr of the target directory')
    parser.add_argument("-H",default='125.140.110.217',help=u'host ip address')
    parser.add_argument("-P",default='44242',help=u'port number')
    parser.add_argument("-l",default=os.getcwd()+separator+'logf.txt',help=u'absolute addr of the log file')
    parser.help=hlp
    args = parser.parse_args()

    #check
    addr = args.addr
    host = args.H
    port = args.P
    log = args.l

    if addr is None:
        exit(u'Required : Absolute address of target directory')
    if host is None:
        print('Proceed host : 125.140.110.217')
    if port is None:
        print('Proceed port : 44242')
    if log is None:
        print('log file in current working directory')


    return (addr, host, port, log)


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

    dt = pd.read_csv(path,encoding=enc)

    

    #column names
    tags = list(dt)

    tags.remove('데이터수신시간')

    div = int(len(tags)/2) + 1
    print(div)
    #div2 = int(len(tags)/3 * 2)

    print(tags)
    print()
    tags1 = tags[0:div]
    print(tags1)
   
    tags2 = [tags[0]]+tags[div:]
    print(tags2)
    #tags3 = [tags[0]]+tags[div2-1:div2+3]
    #print(tags3)
    print()

    

    
    driver_func(dt,tags1)
    driver_func(dt,tags2)
   # driver_func(dt,tags3)

def driver_func(dt,tags):
    global tagnames
    #total num of rows
    length = len(dt)

    for i in range(length): 
        timestamp = timeTOunixtime(str(dt['데이터수신시간'][i]))
        for contentname in tags:
            #if contentname == '누적연료사용량(L)':
             #   print('누적 연료 사용량이 주키')

            value = str(dt[contentname][i])
            tagss = list(set(tags)-set([contentname]))
            #print('tags : '+str(len(tagss)))
            #이부분은 좀 더 보완할 필요가 있음

            tg=''
            for t in tagss:
                tg += ' '+tagnames[t]+'='+str(dt[t][i])
 
            content = 'content='+tagnames[contentname]+tg 
            #print(content)
            _buf = "put %s %s %s %s \n" % ('cartests', timestamp, value, content)
            #print('content='+tagnames[contentname]+'  tags='+tg)
            #print(_buf)
            sock.sendall(_buf.encode())

def recursive_dir_search(addr_target_dir):
    global logf
    global count
    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        logf.write(addr_target_dir)

    if 'scandir' in dir(os):

        for entry in os.scandir(addr_target_dir): # entry : os.DirEntry 객체
            try:
                #entry가 디렉토리인 경우
                if entry.is_dir(follow_symlinks = True):
                    recursive_dir_search(addr_target_dir+separator+entry.name)

                #entry가 파일인 경우
                elif entry.is_file(follow_symlinks = False):
                    if len(entry.name) < 5:
                        continue

                    addr_entry = addr_target_dir + separator + entry.name
                    if entry.name[-4:]== '.csv': #확장자 검사 : 엑셀파일 여부 확인
                        print("writing")
                        ret = Write_to_opts(addr_entry,'euc-kr')
                       # print('%s' % (addr_entry))
                        count += 1

            except OSError:
                logf.write(addr_target_dir+separator+entry.name+'\n')
                #addr_target_dir 파일을 처리하려고 하였으나 예외가 발생한 경우
                #해당 파일의 절대주소를 별도로 저장한다



if __name__ == "__main__":
    addr, host, port, log = parse_args()
    logf = open(log,mode='w+')
    print(host)
    print(port)
    sock.connect((host,int(port)))

    recursive_dir_search(addr)
    logf.close()
    sock.close()
  #  print(count)

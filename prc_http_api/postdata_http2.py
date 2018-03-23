
'''
	*목적 :본 프로그램은 post방식을 사용하여 opentsdb에 데이터를 저장한다
	*사용된 핵심 모듈 :
		-json : 데이터포인트를 http api를 사용하여 넘길 때 opentsdb에서는 default로 json serializer를 사용하기 때문에
			데이터포인트를 json형식으로 만들 때 사용
		-requests : json형식의 데이터포인트를 http api/put을 사용해서 전송할 때 사용되는 모듈이다 (http 통신할 때 사용)
		-pandas : 로컬에 저장된 .csv파일을 읽어서 전처리하는 과정에 사용하였다

	*참고사항 :
		-http://opentsdb.net/docs/build/html/api_http/put.html 를 보면 어떤 형식으로 데이터포인트를 넣어야 하는지 알 수 있다

		-주의할 점은 해당 페이지에 나와있듯이 metric, timestamp, value, tags의 각 값들이 타입이 정확히 나온바와 일치해야한다는 것
		--> else, bad request 발생

		-request에 대한 응답 (response) 객체를 통해 몇개의 데이터포인트가 성공/실패했는지, 나아가 실패한 데이터포인트
		내용까지도 확인 가능하다 (사이트 참고) (response.content에 저장됨)

		-response객체로부터 실패한 데이터포인트가 있을 경우, 해당 데이터포인트 내용을 따로 저장해두었다가 처리하고자 하였으나,
		response.content에 저장된 것은 딕셔너리가 아닌 바이트배열이다....

		-모든 데이터포인트를 한번에 dump해서 보내고자 하는 경우 에러가 발생할 수 있다. 이는 opentsdb 설정을 확인해야한다
			- /etc/opentsdb/opentsdb.conf 중
				-tsd.http.request.enable_chunked 가 false (default)인 경우 기본적으로 max chunk size가 8096이기 때문
				-따라서 tsd.http.reqeust.enable_chunked=true로 설정 후
				       tsd.http.request.max_chunk=사이즈를 설정해주어야한다
'''

import json
import requests
import pandas as pd
import time
import datetime
import sys
import os
import errno

count=0
separator='/'
tot_pd = 0
tot_cs = 0

#opentsdb에는 태그명으로 한글로 할 수 없다.
#읽어들일 파일에 존재하는 컬럼명들을 opentsdb에 저장할 때 사용할 태그명(영어)에 각각 매핑시켜둔다
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

#parse N-datapoints from .csv files
def post_data(path):
    global tot_pd
    global tot_cs
    print('Writing: '+path)

    global count
    _url = 'http://0.0.0.0:44242/api/put?'#sync&sync_timeout=5000'
    headers = {'content-type': 'application/json'}

    metric = '__tttt__'

    dt = pd.read_csv(path, encoding='euc-kr')
	#파일을 읽을 때 사용할 인코딩 설정부
    tags = list(dt)
    #tags = convert_utf8(tags)
    try:
         tags.remove('데이터수신시간')
    except ValueError as e :
	    print(e)

    tags.remove('SET_ID')
    length = len(dt)
    carid = str(dt['SET_ID'][0])
    _buffer =  []##list of dictionaries
    

    count = 0

    st =time.time()
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
            count += 1 #읽어들인 총 데이터포인트 수를 체크하기 위해 설정해두었다


    et =time.time()

    tot_pd += (et-st)

    l = len(_buffer)
    print('BUFFER LEN : ' + str(l))
    
    sess = requests.Session()

    st = time.time()
    for i in range(0,l,100):
            count = 0
            response = sess.post(_url, data = json.dumps(_buffer[i:i+100]), headers= headers)
            time.sleep(0.005) #최적화된 sleep 시간을 지정할 필요가 있다

	#데이터 전송 결과에 대한 응답이 정상이 아닌 경우 해당 데이터포인트를 최대 10번까지 재전송한다
            tries = 0
            while(response.status_code > 204 ) :
                if tries > 10:
                    logf_dp.write('BAD_REQEUST HANDLING : '+ str(_buffer))
                    break

                print('bad request : '+response.status_code)
                time.sleep(1.2) #최적화된 sleep 시간을 지정할 필요가 있다
                response = sess.post(_url, data = json.dumps(_buffer), headers= headers)
                tries += 1
    
    et = time.time()
    tot_cs += (et-st)


def timeTOunixtime (real_time):
    #생략 : re모듈 사용을 통해 주어진 값을 형식화 가능#

    stime = "%s/%s/%s" %(real_time[8:10], real_time[5:7], real_time[0:4])
    sec = int(real_time[11:13])*60*60 + int(real_time[14:16])*60 +int(real_time[17:19])

    unixday = time.mktime(datetime.datetime.strptime(stime, "%d/%m/%Y").timetuple())
    unixtime = unixday + sec
    return unixtime


#재귀적 파일 탐색부
def recursive_dir_search(addr_target_dir):
    global logf
    global total
    #addr_target_dir에 대한 접근 권한 확인
    if not(os.access(addr_target_dir,os.F_OK and os.R_OK)):
        logf.write(addr_target_dir)
        return

    for entry in sorted(os.scandir(addr_target_dir),key=(lambda entry: entry.name)): # entry : os.DirEntry 객체
	#경로내 디렉토리 엔트리를 정렬한 이유 : 정렬하지 않을 경우 해당 엔트리들이 랜덤한 순서로 정렬되어있기 때문에
	#나중에 데이터를 전송하다가 에러가 발생할 경우 어디서부터 진행시킬지 설정할 때 곤란해진다

        try:
            #entry가 디렉토리인 경우
            if entry.is_dir(follow_symlinks = True):
                #if int(entry.name[:10]) < 230
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
                    post_data(addr_entry)
                    print('             | finished writing : '+addr_entry)
                    #성공적으로 전송한 경우 +1

        except OSError as e:
            #permission
            if e.errno == errno.EPERM:
                print('PERMISSION ERROR')
                logf.write('PERMISSION ERROR:'+addr_target_dir+separator+entry.name+'\n')


if __name__ == "__main__":

    logf= open('./faillogs.txt',mode='a') #데이터 전송 실패 시 로그 기록
    logsc = open('./succlogs.txt',mode='a') #데이터 전송 성공 시 로그 기록
    logf_dp = open('./faillogs_dp.txt',mode='a') #성공적으로 전송 및 저장되지 않은 데이터포인트 목록

    recursive_dir_search('/home/jh/201409') #읽어들일 파일 경로 지정
    #recursive_dir_search('/home/teama/testdata2')
    print('Done')
    print('Datapoints saved :' + str(count))

    print('tot_pd :'+str(tot_pd))
    print('tot_cs :'+str(tot_cs))

    logf.close()
    logsc.close()
    logf_dp.close()

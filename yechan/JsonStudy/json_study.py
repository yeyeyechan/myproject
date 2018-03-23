#----------------------------------------------------------------------------------------------------------------------
import json

# python dictionary 객체를 JSON 문자열로 만드는 프로그램

customer ={
    'id':  152352,
    'name': '강진수',
    'history': [
        {'data': '2015-03-11', 'item': 'iphone'},
        {'date': '2016-02-23', 'item':'monitor'}
    ]
}
# JSON 인코딩
jsonString = json.dumps(customer)

print(jsonString)
print(type(jsonString))

# 원래 제이선 스트링은 한줄 -. 보기 좋게 바꾸려면 dumps안에 indent 를 집어넣는다.
jsonString=json.dumps(customer, indent =4)
print(jsonString)

#----------------------------------------------------------------------------------------------------------------------

# JSON 디코딩

import json

jsonString ='{***********************************' # 위의 자료가 한줄의 문자열로 표현된 상태

dict =json.loads(jsonString)

print(dict['name'])
for h in dict['history']:
    print (h['date'], h['item'])

#----------------------------------------------------------------------------------------------------------------------
#이거로 보자

import json
from collections import OrderedDict

file_data= OrderedDict()

file_data["name"]= "computer"
file_data["language"]="kor"
file_data["words"]={'ram':'램',-------------------------}
file_data["number"]=4

print(json.dumps(file_data, ensure_ascii=False, indent ="\t"))

# 위와 같이 제이선 형식으로 출력시엔 json.dumps를 쓴다. ensure_ascii는 아스키로의 변환 안한다는 뜻

with open('words.json','w', encoding ='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False,indent="\t")

# 파일이름을 워드 제이선으로 만들고 인코딩 해주고 넣어줄 데이터와 만들려고 넣어둔 변수를 집어 두고 설정을 해준다. 저장시엔
#dump! not dumps


#----------------------------------------------------------------------------------------------------------------------

#인터넷에서 날씨정보를 받아 json 패키지로 파싱!

import urllib

import json
import datetime

url ='http://api.openweathermap.org/data/2.5/weather?q=Seoul,kr'

u = urllib.urlopen(url)
data= u.read()

j =json.loads(data)

name = j["name"]
print "City name"
print name
print "\n"

dt=j["dt"]
print "Data receving time"
print datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-Wm-%d %H:%M:%S')
print "\n"

weather =j['weather']
main =weather[0]
print main["main"]
print main["description"]






























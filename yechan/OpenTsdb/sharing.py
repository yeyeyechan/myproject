#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
from openpyxl import*
import requests
import json


url = "http://125.140.110.217:44242/api/put"
response ={}


def timeTOunixtime (real_time):

    unixtime = time.mktime(real_time.timetuple())
    return unixtime

def string2celcius(celcius):
    if celcius == None:
        return False
    celcius =float(celcius)

    return celcius

def jsonmetric( unixtime, celcius):

    degree = {
        "metric": u"판교_10일간의_시간별온도변화5",
        "timestamp": unixtime,  # uxtime으로 전환해 주어야 tsdb가 받아들이는 형식과 맞음
        "value": celcius,  # 넣고싶은 값
        "tags": {
            "content": u"판교날씨",

        }
    }

    push = requests.post(url, data=json.dumps(degree), timeout =20)
    return push



if __name__ == "__main__":
    looptime=0


    f=  load_workbook("data.xlsx")
    sheet =f.get_sheet_by_name("Sheet1")

    for i ,k in sheet.rows:

        unixTime = timeTOunixtime(i.value)
        Celcius = string2celcius(k.value)




        if Celcius and unixTime :
            pass
        else:
            continue


        donecheck = jsonmetric( unixTime, Celcius)
        looptime +=1


        if donecheck > 0:
             pass

        else:
            break
        if looptime%1000==0:
            time.sleep(10)


    print u"끝남"

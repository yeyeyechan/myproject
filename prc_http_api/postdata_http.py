'''
다음은 opentsdb에 저장하는 방식 중 http api를 사용하여 데이터포인트를 저장하는 방식을 간단히 구현해보았다 (데이터포인트 2개 입력)
'''


import json
import requests


def post_data():
    st_time = "2014061300"
    ed_time = "2014063000"
    
    metric = 't1'
    tags = '{content=rpm,carid=1}'

    
    
    
    _url = 'http://0.0.0.0:44242/api/put?sync&sync_timeout=10000'
    
    Body = [{#datapoint1
                "metric": 'testposts',
                "timestamp": '1346846400',
                "value": '18',
                "tags": {
                   "content": "rpm",
                   "carid": '1',
                    "bounds_spd" : '1'
                }
             },
             {#datapoint2
                "metric": 'testposts',
                "timestamp": '1346846500',
                "value": '19',
                "tags": {
                   "content": "rpm",
                   "carid": '1',
                    "bounds_spd" : '1'
                } 
             }
            ]      
    
    response = requests.post(_url, data = json.dumps(Body))
    print(response)
    
    
if __name__ == '__main__':
    post_data()

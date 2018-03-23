import urllib.request
import pandas as pd
import os
import json




def read_data():
    st_time = "2014061300"
    ed_time = "2014063000"

    st = "%s/%s/%s-%s:00:00" % (st_time[0:4],st_time[4:6],st_time[6:8],st_time[8:10])
    ed = "%s/%s/%s-%s:00:00" % (ed_time[0:4],ed_time[4:6],ed_time[6:8],ed_time[8:10])

    metric = 't1'
    tags = '{content=rpm}'
    agg = 'sum'

    _url = 'http://0.0.0.0:44242/api/query?'

    tsdb_url = _url+'start='+st+'&end='+ed+'&m='+agg+':'+'rate:'+metric+tags

    response = urllib.request.urlopen(tsdb_url)
    
    data = json.loads(response.read().decode())

    print(type(data)) #list

    #df = pd.DataFrame(data)



    metric = data[0]['metric'] #string
    content = data[0]['tags']['content'] #string
    tagv = data[0]['tags']['carid'] # tagvalue
    timestamps = list(data[0]['dps'].keys()) #list
    values = list(data[0]['dps'].values())



if __name__ == "__main__":
    read_data()


    #rows = len(values)
    #values = [ v for v in values if v >= 30]
    #timestamps = [ t for t in timestamps if data[0][t] >= 30]


    bounds_spd = []
    for t in timestamps:
        v = data[0]['dps'][t]
        bounds_spd.append(1 if v >= 30 else 0)

            
    '''
    new_data = {}
    for t in timestamps:
        v = data[0]['dps'][t]
        if v >= 30:
            new_data[t] = v 
    '''
    
    
    #print(new_data)



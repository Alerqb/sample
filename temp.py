# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#GET https://api.travelpayouts.com/v1/prices/cheap?origin=MOW&destination=HKT&depart_date=2016-11&return_date=2016-12&token=1ec285bda6850f2af14679136e500b20
import urllib.request
contents = urllib.request.urlopen("https://api.travelpayouts.com/v1/prices/cheap?origin=MOW&destination=HKT&depart_date=2018-10&return_date=2018-10&token=1ec285bda6850f2af14679136e500b20").read()
print(contents)

a = "https://api.travelpayouts.com/v1/airline-directions?airline_code=SU&limit=1000&token=1ec285bda6850f2af14679136e500b20"

contents2 = urllib.request.urlopen(a).read()
l = str(contents2).split('"')[1::2][2:-3]
print(l)



import requests
import pandas as pd
import io 

url = "https://api.travelpayouts.com/v1/airline-directions"
querystring = {"airline_code":"SU","limit":"1000"}
headers = {'x-access-token': '1ec285bda6850f2af14679136e500b20'}
response = requests.request("GET", url, headers=headers, params=querystring)
routes = response.text.split('"')[1::2][2:-3]


url = "https://api.travelpayouts.com/v1/prices/calendar"
cur = 'rub'
headers = {'x-access-token': '321d6a221f8926b5ec41ae89a3b2ae7b'}

for each in list(range(1)):
    pair= a[each].split('-')
    querystring = {"depart_date":"2018-10","origin":pair[0],"destination":pair[1],"calendar_type":"departure_date","currency":cur}
    response = requests.request("GET", url, headers=headers, params=querystring)
    df = pd.read_fwf(io.StringIO(response.text))
    df.to_csv('data.csv')
    result_df = pd.read_csv('data.csv',)
    print(result_df.columns)


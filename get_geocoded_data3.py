import pandas as pd
import math

data=pd.read_csv("geocoded_data1.csv")
states={}
for item in data.iterrows():
    for el in item[1][3].split(";"):
        states[el]=item[1][4]
print(states)



all_locations=[]
for item in list(data["location"].unique()):
    all=item.split(";")
    for it in all:
        all_locations.append(it)
print(all_locations)
print(len(all_locations))

data5=pd.read_csv("all_locations.csv")
print(data5)

import requests
all_keys=[]
for item in data5.iterrows():
    #print(item[1]["address"])
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    try:
        if math.isnan(item[1]["address"]):
            location = item[1]["name"].replace(" ","+")
            api_key = 'chTauv-XQTDxbydphqzBEKZ1ZLs4RenX09s-DvuaJFE' # Acquire from developer.here.com
            PARAMS = {'apikey':api_key,'q':location} 

            # sending get request and saving the response as response object 
            r = requests.get(url = URL, params = PARAMS) 
            data2 = r.json()
            print(data2)
            print(list(item[1].values))
            all_keys.append(list(item[1].values))
    except:    
        continue

dd=pd.DataFrame(all_keys,columns=["id","name","state","address","lat","lng"])
dd.to_csv("gazetteer2.csv")


import pandas as pd

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
for item in data5[:1].iterrows():
    print(item[1]["address"])
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    try:
        location ="2800 Rock Creek Pkwy, Kansas City, MO 64117  "
        #item[1]["address"].replace(" ","+")
        api_key = 'chTauv-XQTDxbydphqzBEKZ1ZLs4RenX09s-DvuaJFE' # Acquire from developer.here.com
        PARAMS = {'apikey':api_key,'q':location} 

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        data2 = r.json()

        #latitude = data2['items'][0]['position']['lat']
        #longitude = data2['items'][0]['position']['lng']
        ml=list(item[1].values)
        al=list(data2["items"][0]["position"].values())
        ml[4]=al[0]
        ml[5]=al[1]
        print(ml)
        all_keys.append(ml)
    except:
        print(list(item[1].values))
        all_keys.append(list(item[1].values))
        continue

dd=pd.DataFrame(all_keys,columns=["id","name","state","address","lat","lng"])
dd.to_csv("gazetteer5.csv")


import pandas as pd
import json
dd={}
with open("features.json","r") as fp:
    dd=json.load(fp)

all_data=[]    
data=pd.read_csv("geocoded_data_2.csv")
for item in data.iterrows():
    if item[1][1] not in list(dd.keys()):
        #print(list(item[1].values))
        all_data.append(list(item[1].values))
print(len(all_data))        
data0=pd.DataFrame(all_data,columns=["index","title","description","url","location"])
data0.to_csv("filtered_geocoded.csv")

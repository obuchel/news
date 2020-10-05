
import json
import pandas as pd

kkeys={}
data0=pd.read_csv("list of words.csv")
print(data0)
for item in data0.iterrows():
    if item[1]["category"] not in list(kkeys.keys()):
        kkeys[item[1]["category"]]=[]
        kkeys[item[1]["category"]].append(item[1]["words"])
    else:
        if item[1]["words"] not in kkeys[item[1]["category"]]:
            kkeys[item[1]["category"]].append(item[1]["words"])
    
data11=data0.groupby(["category","words"]).count().reset_index()["words"].to_list()
data12=data0.groupby(["category","words"]).count().reset_index()["category"].to_list()
with open("universities_geojson.json","r") as fp:
    data=json.load(fp)
    for item in data["features"]:
        #print(item["properties"].keys())
        item["properties"]["categories"]=""
        for it in data11:
            if it in item["properties"]["descriptions"]:
                item["properties"]["categories"] += data12[data11.index(it)]+", "
        #print(item["properties"]["categories"])        
    with open("universities_geojson3.json","w") as fp:
        json.dump(data,fp)



    
print(data11)    

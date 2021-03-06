
import pandas as pd
import json
import math
dd0={}
dd1={}

df=pd.read_csv("urls_with_full_texts_sentiments.csv")
full_texts={}

for item in df.iterrows():
    if item[1]["url"] not in list(full_texts.keys()):
        full_texts[item[1]["url"]]=item[1]["description"]

with open("features2.json","r") as fp:
    kk=json.load(fp)
    dd0=kk
with open("features.json","r") as fp:
    kk=json.load(fp)
    dd1=kk

dd = dd0.copy()   # start with x's keys and values
dd.update(dd1)     

names={}
data=pd.read_csv("gazetteer50.csv")
#print(data.values)
for item in data.values:
    #print(list(item)[2])
    names[list(item)[2]]=[list(item)[5],list(item)[6]]
print(names)    
data0=pd.read_csv("gazetteer.csv")
#print(data.values)                                                                                        
for item in data0.values:
    #print(list(item)[2])                                                                                 
    names[list(item)[2]]=[list(item)[5],list(item)[6]]
print(names)    
kkeys={}
data2_=pd.read_csv("filtered_geocoded.csv")
data3=pd.read_csv("geocoded_data1.csv")
data3_=data2_.append(data3)
data_final=data3_.drop_duplicates()
print(data_final)

#print(data2.values)
for item in data_final.values:
    kk=list(item)
    #if len(list(item)[3].split("; "))>1:
        #print(list(item)[3].split("; "))
    for elem in list(item)[3].split("; "):
        try:            
            if elem not in list(kkeys.keys()):
                #print(elem+"_")
                kk1=kk                
                kk1.append(names[elem])
                kkeys[elem]=[kk1]
                #print(kk1)
            else:
                #print(elem)
                kk2=kk
                kk2.append(names[elem])
                kkeys[elem].append(kk2)
                #print(kk2)
        except:
            continue
#print(kkeys["Alma, AL"])

features={}
features["type"]="FeatureCollection"
features["features"]=[]

for item in list(kkeys.keys()):
    #print(item)
    #print(item,kkeys[item][0][5])
    str=""
    for it in kkeys[item]:
        try:
            print(list(full_texts.keys()).index(it[2]))
            str+=it[0]+" _ "+full_texts[it[2]]+" _ "+it[2]+" _ "+dd[it[0]][0]+" _ "+dd[it[0]][1].split("T")[0]+" | "
        except:
            str+=it[0]+" _ "+it[1]+" _ "+it[2]+" _ "+dd[it[0]][0]+" _ "+dd[it[0]][1].split("T")[0]+" | "
            continue
        #str+=it[0]+" _ "+it[1]+" _ "+it[2]+" _ "+dd[it[0]][0]+" _ "+dd[it[0]][1].split("T")[0]+" | "
    temp={'type': 'Feature','geometry': {'type': 'Point','coordinates': [kkeys[item][0][5][1],kkeys[item][0][5][0]]},'properties': {"weight":math.log(len(kkeys[item])+1)*3+4,"name":item,"descriptions":str}} #kkeys[item]
    features["features"].append(temp)
#print(features)

with open("universities_geojson2.json","w") as fp:
    json.dump(features,fp)

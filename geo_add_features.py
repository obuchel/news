import json
import pandas as pd
from glob import glob
files = glob('bing_results_*.json')
print(files)

all_coords={}
dd=pd.read_csv("filtered_geocoded.csv")
kk=dd["title"].to_list()
for el in files:
    print(el)
    try:
        with open(el,"r") as fp:
            data=json.load(fp)
            for item in data["value"]:
                if item["name"] in kk: 
                     all_coords[item["name"]]=[item['provider'][0]["name"], item['datePublished']]
    except:
        continue
print(len(all_coords.keys()))                
with open("features2.json","w") as fp:
    json.dump(all_coords,fp)

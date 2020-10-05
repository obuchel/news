
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
import json
import dload

pagesToGet= 1
data=pd.read_csv("saved_final_data.csv")
urls=list(data["url"].unique())
#print(len(urls)
#https://api.diffbot.com/v3/article?token=b99e00986f2172f9dc81e962bb423c41&url=http%3A%2F%2Fblog.diffbot.com%2Fdiffbots-new-product-api-teaches-robots-to-shop-online
ind=0
for item in urls:
    url="https://api.diffbot.com/v3/article?token=b99e00986f2172f9dc81e962bb423c41&url="+item
    #da=urllib.request.urlopen(url).decode().read()
    data0=dload.json(url)
    with open("json_final_"+str(ind)+".json","w") as fp:
        json.dump(data0,fp)
    ind+=1

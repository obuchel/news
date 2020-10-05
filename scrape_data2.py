

import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
import math
frame=[]
ind=0
data=pd.read_csv("urls_with_tags.csv")
print(data)
for item in data.iterrows():
    url=item[1]["Url"]
    try:
        page=requests.get(url)
    except Exception as e:                                   # this describes what to do if an exception is thrown                           
        error_type, error_obj, error_info = sys.exc_info()      # get the exception information                                              
        print ('ERROR FOR LINK:',url)                          #print the link that cause the problem                                        
        print (error_type, 'Line:', error_info.tb_lineno)
        continue
    #time.sleep(200)
    soup=BeautifulSoup(page.text,'html.parser')
    classes = soup.findAll(item[1]["Tag"])
    soup0=[]
    if item[1]["Tag"]=="article":
        #print(url,item[1]["Tag"])
        link=soup.find("article")
        #print(link)
        soup0=link        
    else:    
        if pd.isna(item[1]["Class"])==False:
            for cl in classes:
                kk=cl.get_attribute_list('class')
                for i in kk:
                    try:
                        if i==item[1]["Class"]:
                            if pd.isna(item[1]["data-source-id"])==False:
                                kkk=cl.get_attribute_list('data-source-id')
                                for ii in kkk:
                                    try:
                                        if str(ii)==str(item[1]["data-source-id"]).split(".")[0]:
                                            #print("__________________________"+ii) #statement
                                            link_1=soup.find(item[1]["Tag"], attrs = {'data-source-id':ii})
                                            soup0=link_1
                                    except:
                                        continue
                            else:
                                #print(url,i) #statement
                                link_2=soup.find(item[1]["Tag"], attrs = {'class':i})
                                soup0=link_2
                    except:
                        continue
        elif pd.isna(item[1]["Id"])==False:
            #print(item[1]["Id"])
            for cl in classes:
                kk6=cl.get('id')
                ih=kk6
                try:
                    if ih==item[1]["Id"]:
                        link_3=soup.find(item[1]["Tag"], attrs = {'id':ih})
                        #print(url,ih) #statement
                        soup0=link_3
                except:
                    continue
        else:
            print(url)
    try:
        for s in soup0.select('script'):
            s.extract()
    except:
        continue
    Title=soup0.find_all('h1')#,attrs={'class':'o-listicle__item'})
    Title2=soup0.find_all('h2')
    
    #print(links)                                                                                                                            
    links2=soup0#,attrs={'class':'photo-credit'})
    #print(links2)
    title=""
    for j in Title:
        try:                                                               
            Statement = j.text.strip()
            title += Statement
        except:
            continue
    for j in Title2:
        try:
            Statement = j.text.strip()
            title += Statement
        except:
            continue    
    st=""
    for j in links2:
        try:
            Statement = j.text.strip()
            st += Statement
        except:
            continue
    #for j in links3:                                                                                                                         
    #    #Statement = j.find("div",attrs={'class':'crd clln--it'})                                                                            
    #    Statement = j.text.strip()                                                                                                           
    #    st += Statement                                                                                                                      
    #print(title,st)                                                                                                                          
    frame.append((Statement,url,title))
    print(Statement)                                                                                                                             
    #with open("frame"+str(ind)+".pkl","wb") as f:                                                                                            
    #pickle.dump(frame, f, pickle.HIGHEST_PROTOCOL)                                                                                           
    ind+=1
fr=pd.DataFrame(frame)
print(fr)
fr.to_csv("trial.csv")

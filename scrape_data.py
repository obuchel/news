
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle
pagesToGet= 1
data=pd.read_csv("geocoded_data_1.csv")
urls=list(data["2"].unique())


upperframe=[]
ind=10
frame=[]
for page in urls[12:20]:
    print('processing page :', page)
    url = page
    #print(url)
    
    #an exception might be thrown, so the code should be in a try-except block
    try:
        #use the browser to get the url. This is suspicious command that might blow up.
        page=requests.get(url)                             # this might throw an exception if something goes wrong.
    
    except Exception as e:                                   # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()      # get the exception information
        print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
        print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
        continue#ignore this page. Abandon this and go back.
    time.sleep(100)
    
    soup=BeautifulSoup(page.text,'html.parser')
    classes = soup.findAll('article')
    #print(classes)
    for cl in classes:
        kk=cl.get_attribute_list('class')
        for i in kk:
            try:
                #print(i)
                if i.index("caas">=0):
                    print(i)
            except:
                continue
        '''    
        kk0=cl.get_attribute_list('article')
        for i in kk0:
            try:
                print(i)
            except:
                continue
            
        kk1=cl.get_attribute_list('id')    
        for i in kk1:
            try:
                print("id "+i)
                if i.index("article")>=0 or i.index("content")>=0 or i.index("maincontent")>=0 or i.index("caas-body">=0):
                    print(i)
            except:
                continue
                kk1=cl.get_attribute_list('id')
        kk2=cl.get_attribute_list('section')        
        for i in kk2:
            try:
                #print("id "+i)
                print(i)
            except:
                continue
        '''    
    '''
    for cl in classes:
        if cl.index("article")>0:
            frame=[]
    '''
    for s in soup.select('script'):
        s.extract()
    
    Title=soup.find_all('h1')#,attrs={'class':'o-listicle__item'})                                        
    #print(links)
    links2=soup.find_all('div')#,attrs={'class':'photo-credit'})
    #print(links2)
    #links3=soup.find_all('div',attrs={'class':cl})
    #print(type(links3))
    #print(links[0]+" "+links2[0]+" "+links3[0])
    '''
    wrapper clearfix pb-curated full pb-feature pb-layout-item pb-f-article-body
    filename="NEWS.csv"
    f=open(filename,"w", encoding = 'utf-8')
    headers="Statement,Link,Date, Source, Label\n"
    f.write(headers)
    '''
    title=""
    for j in Title:
    #Statement = j.find("div",attrs={'class':'crd clln--it'})                                 
        Statement = j.text.strip()
        title += Statement
        st=""    
    for j in links2:
        #Statement = j.find("div",attrs={'class':'crd clln--it'})                                 
        Statement = j.text.strip()
        st += Statement
    #for j in links3:
    #    #Statement = j.find("div",attrs={'class':'crd clln--it'})
    #    Statement = j.text.strip()
    #    st += Statement
    #print(title,st)    
    frame.append((Statement,url,title))
    #print(frame)
    #with open("frame"+str(ind)+".pkl","wb") as f:
    #pickle.dump(frame, f, pickle.HIGHEST_PROTOCOL)
    ind+=1    


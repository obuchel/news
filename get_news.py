#from eventregistry import *
import json
import urllib.request
import sys
#er = EventRegistry(apiKey = "068bacd1-4c7e-42aa-9868-23bec0104ea8")

titles=["MIT moves business school classes online for a week in response to student gatherings","President Michael Crow: No furloughs, layoffs or program eliminations expected at ASU due to COVID-19","Student claims roach-infested college gave one roll of toilet paper to quarantiners","Despite parent protests, Pritzker says he’s following experts in delaying high school sports","Kansas Relays to be postponed from 2021 date due to COVID-19","Madison, Dane County officials 'very concerned' about fans clustering for UW football games","Governor Won't Exclude SDSU COVID-19 Cases From County Figures","More B-Schools Join The Test Optional Bandwagon","USA Today columnist says decision to play football is ‘darkest day’ in Big Ten history, overlooks Sandusky, Nassar scandals","Boise State president's memo says there will be cuts in jobs, operations","Chris Akkerman, Crescent Heights schools declare COVID-19 outbreaks; 171 new cases in Alberta - Calgary Herald","We Run Down the COVID-19 Situation on Big Ten Campuses. It's Not Pretty","Midday Edition Special: Coronavirus Impacts On Vulnerable Students","This Is Not How I Pictured My Senior Year of College. But It’s Not All Bad Either","West Virginia University Demonstrates COVID-19 Hypocrisy In Higher Education","Big Ten neither requested nor received federal support in return to play 2020 college football seasonUtah reports 747 cases of COVID-19 — the most in a day since July — and a record 48 new cases in schools - Salt Lake Tribune","Hey Big Ten, How About Daily COVID Testing for My Kid?","As schools spend big on temperature check tech, experts warn: They won't work","NCSC steps up ransomware support for schools and universities","Health department extends Lincoln, Lancaster County mask mandate through Halloween"]




url="http://eventregistry.org/api/v1/event/getEventsForTopicPage?uri=23139dba-1eef-4adb-996c-4b7e85237aca&resultType=events&eventsSortBy=date&includeEventSummary=true&eventImageCount=1&includeConceptDescription=true&includeSourceDescription=true&storyImageCount=1&eventsPage=2&eventsCount=200&apiKey=068bacd1-4c7e-42aa-9868-23bec0104ea8"

for i in range(6,118):
    url2="http://newsapi.org/v2/everything?q=outbreak&from=2020-08-17&page="+str(i)+"&sortBy=publishedAt&apiKey=05abbd322083446298367e947cbdc3e1"
    try:
        with urllib.request.urlopen(url2) as f:
        
            dd=f.read().decode('utf-8')
            print(dd)
            #dd=data.read().decode(data.headers.get_content_charset())
            with open("file"+str(i)+".json","w") as file_open:
                file_open.write(dd)
    except:
        print(sys.exc_info()[0])
        continue

#http://eventregistry.org/api/v1/event/getEventsForTopicPage?uri=covid&resultType=events&eventsSortBy=date&includeEventSummary=true&eventImageCount=1&storyImageCount=1&apiKey=068bacd1-4c7e-42aa-9868-23bec0104ea8&callback=JSON_CALLBACK
#q = QueryEvent("eng-2940883")

'''

http://eventregistry.org/api/v1/event/getEventsForTopicPage?uri=23139dba-1eef-4adb-996c-4b7e85237aca&resultType=events&eventsSortBy=date&includeEventSummary=true&eventImageCount=1&includeConceptDescription=true&includeSourceDescription=true&storyImageCount=1&page=2&apiKey=068bacd1-4c7e-42aa-9868-23bec0104ea8




q = QueryArticlesIter("eng-2940883",lang = [ "eng" ],
    keywords = QueryItems.OR(["Coronavirus", "outbreak","US"]))
# obtain at most 500 newest articles or blogs
for art in q.execQuery(er, sortBy = "cosSim", maxItems = 1000):
    print(art)
'''
'''
requestEventArticleTrend = RequestEventArticleTrend(
    lang = [ "eng"],
    page = 1,
    count = 100
)
q.setRequestedResult(requestEventArticleTrend)

res = er.execQuery(q)

for art in res:
    print(art)

recentQ = GetRecentEvents(er)

starttime = time.time()
while True:
    eventList = recentQ.getUpdates()
    print("=======%d events were added since the last call" % len(eventList))

    for event in eventList:
        print(event)

    print("sleeping for 60 seconds...")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))



'''



'''
https://eventregistry.org/api/v1/article/getArticles?resultType=articles&keyword=school&keyword=COVID&keywordOper=or&lang=eng&articlesSortBy=date&includeArticleConcepts=true&forceMaxDataTimeWindow=31&apiKey=
'''
                                



'''
import requests

url = "https://necsi.p.rapidapi.com/"

payload = ""
headers = {
    'x-rapidapi-host': "necsi.p.rapidapi.com",
    'x-rapidapi-key': "c960d37eafmsh28f1d44f271c985p16eda5jsn7007f45e1a19",
    'content-type': "application/x-www-form-urlencoded"
    }
params={"parameter1": 'COVID' }
response = requests.request("", url, data=payload, headers=headers, params=params)

print(response.text)
'''

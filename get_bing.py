

#https://azure.microsoft.com/en-us/pricing/details/cognitive-services/search-api/

#https://api.cognitive.microsoft.com/bing/v7.0/news/search?q=COVID-19 outbreak school university&count=100&page=1&key=fc07996ef6f54e09b8af63f3fc4ea697
import json
import requests
new=6
subscription_key = "d64f19ae34174105a5c52640b931ca23"
search_term = "COVID-19 outbreak university"
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
#params  = {"q": search_term,"cc":"US", "count":100,"page":new,"headlineCount":500,"textDecorations": True, "textFormat": "HTML"}
#key 2: 1657acd10f614d2cae49a71e6720d52a

for en in range(3000,4001):
    print(en*100)
    params  = {"q": search_term,"cc":"US", "offset":en*100,"first":en*100,"count":100,"textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    #descriptions = [article["description"] for article in search_results["value"]]
    #https://signup.azure.com/signup?offer=ms-azr-0044p&appId=102&ref=azureplat-generic&redirectURL=https:%2F%2Fazure.microsoft.com%2Fen-ca%2Fget-started%2Fwelcome-to-azure%2F&l=en-ca&correlationId=1FE24052742366D3007F4D1A702365A8
    print(search_results)
    ss=response.json()
    with open("bing_results_10_"+str(en)+".json","w") as openF:
        json.dump(ss,openF)

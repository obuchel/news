import requests

url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetTopNews"

headers = {
    'x-rapidapi-host': "myallies-breaking-news-v1.p.rapidapi.com",
    'x-rapidapi-key': "c960d37eafmsh28f1d44f271c985p16eda5jsn7007f45e1a19"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


import string
import pandas as pd

data=pd.read_csv("urls_with_full_texts_sentiments.csv")
data["title_description"]=data["title"]+" "+data["description"]
list_form=data["title_description"].to_list()
print(list_form)
list_form0=[str(x).replace("\n"," ").lower().translate(str.maketrans('','',string.punctuation)) for x in list_form]
corpus=[]
for text in list_form0:
    corpus.append([l for l in text])
print(list_form0)
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english', min_df=2, max_df=0.5)
tfs = tfidf.fit_transform(list_form0)
print(tfidf)
    
import random
#i = random.randint(0, len(list_form0))
#print(corpus[i])
feature_names = tfidf.get_feature_names()
print(feature_names)
for i in range(0,len(list_form0)):
    response = tfidf.transform([list_form0[i]])
    #print(response)
    keywords = []
    for col in response.nonzero()[1]:
        #print(feature_names[col])
        keywords.append([feature_names[col], response[0, col]])
    
    ss=sorted(keywords, key= lambda x: -x[1])[:20]
    print(ss)

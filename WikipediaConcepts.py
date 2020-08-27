#!/usr/bin/env python
# coding: utf-8

# In[11]:


import nltk
import string
nltk.download('stopwords')
from os import listdir
from os.path import isfile, join
import pandas as pd
import os
import requests

URL = "http://www.wikifier.org/annotate-article"

#Calc tfidf and cosine similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def generateNewFiles():
    path = "/all"
    df = pd.read_csv(os.path.join(path,"file.csv"), skipinitialspace=True, usecols=["body", "title", "publisher"])
    count = 1
    for row in df.itertuples(index=True, name='Pandas'):
        if(count >= 203):
            E1 = row.body;
            if len(E1)> 10000:
                E1 = E1[0:9999]
            newKeywords = getAnnotations(E1, "en")
            try:
                listToStr = "\n".join([str(elem) for elem in newKeywords]) 
                newPath = "C:/AbdulSittar/Slovenia/Courses/FinalDS/Sports_Events_Data/FIFA-World-Cup/deu/"
                outFile = open(os.path.join(newPath, "German"+str(count)+".txt"), 'w', encoding="utf-8")
                outFile.write(listToStr);
                outFile.close()
            except:
                print("failed")
        count = count + 1;


def getAnnotations(text, lang):
    PARAMS = {'userKey':"dghkpndmjyjtaiyzeswmcpsgfwpnth", "text": text, "secondaryAnnotLanguage": lang}
    r = requests.post(url = URL, data = PARAMS)
    try:
        data = r.json()
        langAnotations = [];
        if "annotations" in data:
            count = len(data['annotations'])
            annotations = data['annotations']
            for x in annotations:
                if "secTitle" in x:
                    title = x['secTitle']
                    if len(title.split())  > 1:
                        title =  "-".join(title.split(" ")) 
                        langAnotations.append(title)
                    else:
                        langAnotations.append(title)
        return langAnotations;
    except:
        print("failed")


def main(printResults=True):
    generateNewFiles()


main()






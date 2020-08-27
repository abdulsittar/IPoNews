#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import string
import json
import eventregistry
from eventregistry import *
KEY = "b198299a-bb74-4eab-8d59-9dc1fc3679c2"
er = EventRegistry(apiKey = KEY)
dPath = "DataSet/Sports_Events_Data"; #Climate_Changes_Data"   #Natural_Disasters_Data"; #Sports_Events_Data";


EVENT= "FIFA World Cup" #"Global Warming" #"EarthQuake" #"FIFA World Cup"
year= "all"
NUMBER_OF_ARTICLES = 100
Languages = ["eng", "por", "slv", "deu", "spa"]


folder = "-".join(EVENT.split())
dPath = os.path.join(os.path.join(os.path.join(dPath, folder),Languages[4]),year)
print(dPath);
if not os.path.exists(dPath):
    os.makedirs(dPath)


eventUri = er.getConceptUri(EVENT)
q = QueryArticlesIter(keywords = EVENT , lang = Languages[4], sourceUri = None )


oFile2 = open(os.path.join(dPath,"file.csv"), 'wb')
oFile3 = open(os.path.join(dPath,"JSON.csv"), 'w+')
str1 = "language,publisher,title,datetime,body,sourceUri,image,wgt,relevance,url,uri,isduplicate,sim,sentiment"
oFile2.write(str1.encode('utf-8'))
oFile2.write('\n'.encode('utf-8'))
for x in range(0, 10):
    q.setRequestedResult(RequestArticlesInfo(page = x+1, count = 100))
    res = er.execQuery(q)
    oFile3.write(json.dumps(res, indent=2))
    for article in res["articles"]["results"]:
        language = article["lang"]
        SourceTitle = article["source"]["title"].replace(",","-")
        title = article["title"].replace(",","-")
        date = article["dateTime"]
        text = article["body"].replace(",","-")
        text = text.replace(",","-")
        text = text.replace("\n","-")
        sourceUri =  article["source"]["uri"].replace(",","-")
        image = article["image"]
        try:
            image = image.replace(",","-")
        except:
            print("not possible")
        
        wgt = article["wgt"]
        try:
            wgt=wgt.replace(",","-")
        except:
            print("not possible")
        relevance = article["relevance"]
        url = article["url"]
        url = url.replace(",","-")
        uri = article["uri"]
        isduplicate = article["isDuplicate"]
        sim = article["sim"]
        sent = article["sentiment"]

        
        if sent is None:
            sent = "None"
        if image is None:
            image = "None"
        
        str2 = language+","+SourceTitle+","+title+","+date+","+text+","+sourceUri+","+image+","+str(wgt)+","+str(relevance)+","+url+","+str(uri)+","+str(isduplicate) +","+str(sim)+","+str(sent) 
        oFile2.write(str2.encode('utf-8'))
        oFile2.write('\n'.encode('utf-8'))


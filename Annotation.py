#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
data = pd.read_csv("/NewAnnotatedDS.csv")
from datetime import datetime
import array

count = 0
inds = []
for index, row in data.iterrows():
    a = row['source']
    b = row['target']
    s = pd.to_datetime(row['source-time'], format="%Y-%m-%dT%H:%M:%SZ")
    t = pd.to_datetime(row['target-time'], format="%Y-%m-%dT%H:%M:%SZ")
    if s > t:
        inds.append(index1)
        count = count + 1
        
inds = list(dict.fromkeys(inds))
for a in inds:
    print(a);
    data.drop(a , inplace=True)
    print("\n")

data.to_csv('/AnnotatedDataSetSDated.csv')



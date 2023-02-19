#!/usr/bin/env python
# coding: utf-8

# In[56]:
from app import *

import pandas as pd
import numpy as np


from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Main Code

def getColleges(location, budget, satmath, satread, act):
    newdf = pd.read_csv("newdata4.csv")

    ## nans

    newdf.iloc[:,[20,21,22,23,24,25]]=newdf.iloc[:,[20,21,22,23,24,25]].fillna(0)

    newdf = newdf.dropna()

    newdf = newdf[(newdf["IC2021.Academic"]=="Yes") & (newdf["IC2021.Other degree"]=="Implied no")]

    newdf = newdf.drop(['ADM2021.Admission test scores','IC2021.Academic','IC2021.Other degree','year',"HD2021.Degree-granting status","HD2021.Bureau of Economic Analysis (BEA) regions","unitid","HD2021.Institutional category"],axis=1)

    ## cleaning

    resultcols = newdf.iloc[:, [0,1,2,7,8,9,10,11]]

    traincols = newdf.drop(newdf.columns[[0,1,2,7,8,9,10,11]],axis = 1)

    traincols['meanACT'] = traincols[['ADM2021.ACT Composite 25th percentile score', 'ADM2021.ACT Composite 75th percentile score']].mean(axis=1)

    traincols['meanSATmath'] = traincols[['ADM2021.SAT Math 25th percentile score', 'ADM2021.SAT Math 75th percentile score']].mean(axis=1)

    traincols['meanSATread'] = traincols[['ADM2021.SAT Evidence-Based Reading and Writing 75th percentile score', 'ADM2021.SAT Evidence-Based Reading and Writing 25th percentile score']].mean(axis=1)

    traincols=traincols.drop(columns=[
        'ADM2021.SAT Evidence-Based Reading and Writing 25th percentile score', 
        'ADM2021.SAT Evidence-Based Reading and Writing 75th percentile score', 
        'ADM2021.SAT Math 25th percentile score', 
        'ADM2021.SAT Math 75th percentile score', 
        'ADM2021.ACT Composite 25th percentile score','ADM2021.ACT Composite 75th percentile score' ])

    tester = traincols[["IC2021_AY.Out-of-state average tuition for full-time undergraduates","meanACT"]]

    # modeling

    scaler = MinMaxScaler()

    transformtest = scaler.fit_transform(traincols)

    # this is where you put stuff!!!

    print('hello')
    if (location==1):
        instate = budget
        outstate = 0
    else:
        instate = 0
        outstate = budget

    # to be implemented: graduate school
    instategrads = 0
    outstategrads = 0

    user_features = np.array([instate,outstate,instategrads,outstategrads,act, satmath,satread])  # likes drama, action, and thriller movies

    print('hi')
    # Convert user data into vectors

    wherezero = []
    wheredelete=[]
    for x in range(len(user_features)):
        if user_features[x] !=0:
            wherezero.append(traincols.columns[x])
        else:
            wheredelete.append(x)

    user_features=scaler.transform(user_features.reshape(1, -1))

    newfeatures=user_features[user_features!=0]

    tempdf=np.delete(transformtest, wheredelete,1)

    similarity_scores = cosine_similarity(newfeatures.reshape(1,-1), tempdf)

    # Rank items by similarity
    recommendations = np.argsort(-similarity_scores)

    class college:
        def __init__(self,name,state,appfee,roomboard,applicantmen,applicantwom,admissionmen,admissionwom):
            self.name = name
            self.state = state
            self.appfee = appfee
            self.roomboard = roomboard
            self.applicantmen = applicantmen
            self.applicantwom = applicantwom
            self.admissionmen = admissionmen
            self.admissionwom = admissionwom

    topfive = []
    for i in range(5):
    #     print(tempcol)
        tempcol = resultcols.iloc[recommendations[0][i]]
        tempob = college(tempcol[0],tempcol[1],tempcol[2],tempcol[3],tempcol[4],tempcol[5],tempcol[6],tempcol[7])
        topfive.append(tempob)


    print(topfive)



    # In[ ]:





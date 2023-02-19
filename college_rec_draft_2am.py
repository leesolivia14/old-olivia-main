# modules

import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


def getColleges(location, budget, satread, satmath, act):
    # download and clean data

    ## get data
    newdf = pd.read_csv("newdata4.csv")

    ## replace NaNs in SAT and ACT with zero
    newdf.iloc[:,[20,21,22,23,24,25]] = newdf.iloc[:,[20,21,22,23,24,25]].fillna(0)

    ## drop NaNs in other rows
    newdf = newdf.dropna()

    ## drop non-academic institutions
    newdf = newdf[(newdf["IC2021.Academic"]=="Yes") & (newdf["IC2021.Other degree"]=="Implied no")]

    ## drop unnecessary features
    newdf = newdf.drop(['ADM2021.Admission test scores',
                        'IC2021.Academic', 
                        'IC2021.Other degree',
                        'year',"HD2021.Degree-granting status",
                        "HD2021.Bureau of Economic Analysis (BEA) regions", 
                        "unitid", "HD2021.Institutional category"],axis=1)

    ## create a dataframe for the results
    resultcols = newdf.iloc[:, [0,1,2,7,8,9,10,11]]

    ## drop the result columns from the target vectors
    feature_vectors = newdf.drop(newdf.columns[[0,1,2,5,6,7,8,9,10,11]],axis = 1)

    # process data

    ## calculate the mean test scores from the percentile data
    feature_vectors['meanACT'] = feature_vectors[['ADM2021.ACT Composite 25th percentile score', 'ADM2021.ACT Composite 75th percentile score']].mean(axis=1)
    feature_vectors['meanSAT'] = (feature_vectors[['ADM2021.SAT Math 25th percentile score', 'ADM2021.SAT Math 75th percentile score']].mean(axis=1) + feature_vectors[['ADM2021.SAT Evidence-Based Reading and Writing 75th percentile score', 'ADM2021.SAT Evidence-Based Reading and Writing 25th percentile score']].mean(axis=1))

    ## drop the columns that we transformed
    feature_vectors=feature_vectors.drop(columns=[
        'ADM2021.SAT Evidence-Based Reading and Writing 25th percentile score', 
        'ADM2021.SAT Evidence-Based Reading and Writing 75th percentile score', 
        'ADM2021.SAT Math 25th percentile score', 
        'ADM2021.SAT Math 75th percentile score', 
        'ADM2021.ACT Composite 25th percentile score','ADM2021.ACT Composite 75th percentile score' ])

    ## scale the feature vectors
    scaler = MinMaxScaler()
    transformed_features = scaler.fit_transform(feature_vectors.to_numpy())

    # INPUT VECTOR IS HERE

    ## this is where you put stuff!!!
    instate = 0
    outstate = 0

    if (location==1):
        instate = budget
        outstate = 0
    elif (location==0):
        instate = 0
        outstate = budget

    sat = satmath + satread
    #user_features = np.array([instate,outstate,instategrads,outstategrads,act, satmath,satread])
    #user_features = np.array([0,80000,0,800])  
    user_features = np.array([instate, outstate, act, sat], dtype=object)
    # ungrad_instate, undergrad_outstate, grad_instate, grad_outstate, meanACT, meanSAT

    ## scale the input vector
    user_features = scaler.transform(user_features.reshape(1, -1))

    ## save nonzero rows in input vector only
    processed_user_features = user_features[user_features!=0]

    ## delete columns from data where user features are zero
    processed_feature_data = np.delete(transformed_features, np.where(user_features == 0)[1],1)

    # model

    ## calculate cosine simularity between user features
    similarity_scores = cosine_similarity(processed_user_features.reshape(1,-1), processed_feature_data)

    ## Rank items by similarity
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

        def __str__(self):
            return ','.join([str(self.name), str(self.state), str(self.appfee), str(self.roomboard)])

    topfive = []
    for i in range(5):
        #print(tempcol)
        tempcol = resultcols.iloc[recommendations[0][i]]
        tempob = college(tempcol[0],tempcol[1],tempcol[2],tempcol[3],tempcol[4],tempcol[5],tempcol[6],tempcol[7])
        topfive.append(tempob)

    class user:
        def __init__(self, state=None, in_state=False, sat=0, act=0):
            self.state = state
            self.in_state = in_state
            self.sat = sat
            self.act = act

    result_list = [0,0,0,0,0]
    result_dict = {}

    c = 0
    for x in topfive:
       # print(x)
        
        result_list[0] = x
        

        result_parsed = str(x).split(',')

        #print(result_parsed)
        college_name = result_parsed[0]
        result_dict[c] = {'name':result_parsed[0],'state':result_parsed[1], 'appfee': result_parsed[2], 'roomboard': result_parsed[3]}
        #print(result_dict[c])
        
        #print(x)
        '''
        for y in x:
            result[c] = y
            print(result[c])
        '''
        c += 1
    
    #result_dict.update({'name': result_list})

    #print(result_dict)



    return result_dict
            
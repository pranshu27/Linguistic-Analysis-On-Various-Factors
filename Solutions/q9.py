#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 11:20:24 2021

@author: pranshu
"""
import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

total_dict = {}

def createDict(item0, item1):
    tmp = dict()
    tmp['males'] = item0
    tmp['females'] = item1
    return tmp

df = pd.read_excel('c08/DDW-0100C-08.xlsx')
df = df[(df['Unnamed: 2']=='000') & (df['C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011']=='All ages') & \
            (df['Unnamed: 4']=='Total') ]

for f in os.listdir('c08'):
    lst = []
    df = pd.read_excel('c08/'+f)
    df= df.iloc[5:,:]
    df = df[(df['Unnamed: 2']=='000') & (df['C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011']=='All ages') & \
            (df['Unnamed: 4']=='Total') ]
    df.reset_index(drop=True, inplace=True)
    state =  df.loc[0, 'Unnamed: 1']
    df.reset_index(inplace=True, drop=True)
    lst.append(createDict(df.loc[0, 'Unnamed: 10'],df.loc[0, 'Unnamed: 11']) )
    lst.append(createDict(df.loc[0, 'Unnamed: 13'],df.loc[0, 'Unnamed: 14']))
    lst.append(createDict(df.loc[0, 'Unnamed: 19'],df.loc[0, 'Unnamed: 20']))
    lst.append(createDict(df.loc[0, 'Unnamed: 22'],df.loc[0, 'Unnamed: 23']))
    lst.append(createDict(df.loc[0, 'Unnamed: 25'],df.loc[0, 'Unnamed: 26']))
    lst.append(createDict(df.loc[0, 'Unnamed: 28']+df.loc[0, 'Unnamed: 31']+df.loc[0, 'Unnamed: 34']+df.loc[0, 'Unnamed: 37'], \
                          df.loc[0, 'Unnamed: 29']+df.loc[0, 'Unnamed: 32']+df.loc[0, 'Unnamed: 35']+df.loc[0, 'Unnamed: 38']))
    lst.append(createDict(df.loc[0, 'Unnamed: 40'],df.loc[0, 'Unnamed: 41']))
    total_dict[state]=lst
    

df1 = pd.read_excel('DDW-C19-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']!='Total')]

df1.columns
# =============================================================================
# Index(['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX',
#        'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5',
#        'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'],
#       dtype='object')
# =============================================================================


df1 = df1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX', 'Unnamed: 2','Unnamed: 4','Unnamed: 9', 'Unnamed: 10', 'Unnamed: 6', 'Unnamed: 7' ]]

df1.columns = ['State-Code', 'State-Name','Literacy-group','3+Males', '3+Females', '2Males', '2Females']


df1.reset_index(drop=True, inplace=True)



lst = []

all_codes = set(df1['State-Code'])

for code in all_codes:
    tmp_df = df1[df1['State-Code']==code]
    tmp_df.reset_index(drop=True, inplace=True)
    for i in range(len(tmp_df)):
        tmp_df.loc[i, 'Total_Males'] = total_dict[code][i]['males']
        tmp_df.loc[i, 'Total_Females'] = total_dict[code][i]['females']
    lst.append(tmp_df)
        
  
df1 = pd.concat(lst)

df1['3+_pct_males'] = df1['3+Males']/df1['Total_Males']
df1['3+_pct_females'] = df1['3+Females']/df1['Total_Females']

#.drop(['State-Name', '3+', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)

all_states = set(df1['State-Code'])


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx_males = tmp['3+_pct_males'].max()
    maxx_females = tmp['3+_pct_females'].max()
    t['state/ut'] = state
    t['literacy-group-males'] = tmp[tmp['3+_pct_males']==maxx_males]['Literacy-group'].values[0]
    t['ratio-of-3-males'] = maxx_males
    t['literacy-group-females'] = tmp[tmp['3+_pct_females']==maxx_females]['Literacy-group'].values[0]
    t['ratio-of-3-females'] = maxx_females
    out.append(t)
    
    
df = pd.DataFrame(out)
df.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']
df.sort_values('state/ut', inplace=True)
df.to_csv('output/literacy-gender-a.csv', index=False)


















df1['1Males'] = df1['Total_Males'] - df1['2Males']
df1['1Females'] = df1['Total_Females'] - df1['2Females']


df1['2Males'] =   df1['2Males']  - df1['3+Males']
df1['2Females'] = df1['2Females']  - df1['3+Females']


df1['2_pct_males'] = df1['2Males']/df1['Total_Males']
df1['2_pct_females'] = df1['2Females']/df1['Total_Females']

#.drop(['State-Name', '2', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)

all_states = set(df1['State-Code'])


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx_males = tmp['2_pct_males'].max()
    maxx_females = tmp['2_pct_females'].max()
    t['state/ut'] = state
    t['literacy-group-males'] = tmp[tmp['2_pct_males']==maxx_males]['Literacy-group'].values[0]
    t['ratio-of-2-males'] = maxx_males
    t['literacy-group-females'] = tmp[tmp['2_pct_females']==maxx_females]['Literacy-group'].values[0]
    t['ratio-of-2-females'] = maxx_females
    out.append(t)
    
    
df = pd.DataFrame(out)
df.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']

df.sort_values('state/ut', inplace=True)

df.to_csv('output/literacy-gender-b.csv', index=False)













df1['1_pct_males'] = df1['1Males']/df1['Total_Males']
df1['1_pct_females'] = df1['1Females']/df1['Total_Females']

#.drop(['State-Name', '1', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)

all_states = set(df1['State-Code'])


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx_males = tmp['1_pct_males'].max()
    maxx_females = tmp['1_pct_females'].max()
    t['state/ut'] = state
    t['literacy-group-males'] = tmp[tmp['1_pct_males']==maxx_males]['Literacy-group'].values[0]
    t['ratio-of-1-males'] = maxx_males
    t['literacy-group-females'] = tmp[tmp['1_pct_females']==maxx_females]['Literacy-group'].values[0]
    t['ratio-of-1-females'] = maxx_females
    out.append(t)
    
    
df = pd.DataFrame(out)
df.columns = ['state/ut', 'literacy-group-males', 'ratio-males','literacy-group-females', 'ratio-females']

df.sort_values('state/ut', inplace=True)
df.to_csv('output/literacy-gender-c.csv', index=False)



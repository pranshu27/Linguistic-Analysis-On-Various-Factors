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



for f in os.listdir('c08'):
    lst = []
    df = pd.read_excel('c08/'+f)
    df= df.iloc[5:,:]
    df = df[(df['Unnamed: 2']=='000') & (df['C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011']=='All ages') & \
            (df['Unnamed: 4']=='Total') ]
    df.reset_index(drop=True, inplace=True)
    state =  df.loc[0, 'Unnamed: 1']
    df.reset_index(inplace=True, drop=True)
    lst.append(df.loc[0, 'Unnamed: 9'])
    lst.append(df.loc[0, 'Unnamed: 12'])
    lst.append(df.loc[0, 'Unnamed: 18'])
    lst.append(df.loc[0, 'Unnamed: 21'])
    lst.append(df.loc[0, 'Unnamed: 24'])
    lst.append(df.loc[0, 'Unnamed: 27']+df.loc[0, 'Unnamed: 30']+df.loc[0, 'Unnamed: 33']+df.loc[0, 'Unnamed: 36'])
    lst.append(df.loc[0, 'Unnamed: 39'])
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


df1 = df1[['C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX', 'Unnamed: 2','Unnamed: 4','Unnamed: 8', ]]

df1.columns = ['State-Code', 'State-Name','literacy-group','3+']


#df1 = df1[df1['State-Name']!='INDIA']
df1.reset_index(drop=True, inplace=True)


lst = []

all_codes = set(df1['State-Code'])

for code in all_codes:
    tmp_df = df1[df1['State-Code']==code]
    tmp_df.reset_index(drop=True, inplace=True)
    for i in range(len(tmp_df)):
        tmp_df.loc[i, 'Total'] = total_dict[code][i]
    lst.append(tmp_df)
   # print(len(tmp_df))
    
  
df1 = pd.concat(lst)


df1['3+_pct'] = df1['3+']*100/df1['Total']

df1.drop(['State-Name', '3+', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)

all_states = set(df1['State-Code'])


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx = tmp['3+_pct'].max()
    t['state/ut'] = state
    t['literacy-group'] = tmp[tmp['3+_pct']==maxx]['literacy-group'].values[0]
    t['percentage'] = maxx
    out.append(t)
    
    
df = pd.DataFrame(out)
df.sort_values('state/ut', inplace=True)
df.to_csv('output/literacy-india.csv', index=False)



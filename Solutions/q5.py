#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:17:04 2021

@author: pranshu
"""
import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd


'''
df.columnsIndex(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3',
       'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ',
       'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
       'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'],
      dtype='object')


'''

total_dict = {}

for f in os.listdir('c14'):
    lst = []
    df = pd.read_excel('c14/'+f, sheet_name='Sheet1')
    df= df.iloc[7:,:]
    df = df[df['Unnamed: 2']=='000']
    df.reset_index(drop=True, inplace=True)
    state =  df.loc[0, 'Unnamed: 1']
    
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='5-9']['Unnamed: 5'].values[0])
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='10-14']['Unnamed: 5'].values[0])
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='15-19']['Unnamed: 5'].values[0])
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='20-24']['Unnamed: 5'].values[0])
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='25-29']['Unnamed: 5'].values[0])
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='30-34']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='35-39']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='40-44']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='45-49']['Unnamed: 5'].values[0]
               )
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='50-54']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='55-59']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='60-64']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='65-69']['Unnamed: 5'].values[0]
               )
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='70-74']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='75-79']['Unnamed: 5'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='80+']['Unnamed: 5'].values[0]
               )
    
    lst.append(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='Age not stated']['Unnamed: 5'].values[0])

    total_dict[state] = lst
    
    





df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']!='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2','Unnamed: 4','Unnamed: 8', ]]

df1.columns = ['State-Code', 'State-Name','Age-group','3+']

df1.reset_index(drop=True, inplace=True)

#df1 = df1[df1['State-Name']!='INDIA']


lst = []

all_codes = set(df1['State-Code'])

for code in all_codes:
    tmp_df = df1[df1['State-Code']==code]
    tmp_df.reset_index(drop=True, inplace=True)
    for i in range(len(tmp_df)):
        tmp_df.loc[i, 'Total'] = total_dict[code][i]
    lst.append(tmp_df)
        
  
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
    t['age-group'] = tmp[tmp['3+_pct']==maxx]['Age-group'].values[0]
    t['percentage'] = maxx
    out.append(t)
    
df = pd.DataFrame(out)
df.sort_values('state/ut', inplace=True)
df.to_csv('output/age-india.csv', index=False)




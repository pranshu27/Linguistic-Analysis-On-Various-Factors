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


total_dict = {}

def createDict(item0, item1):
    tmp = dict()
    tmp['males'] = item0
    tmp['females'] = item1
    return tmp

for f in os.listdir('c14'):
    lst = []
    df = pd.read_excel('c14/'+f, sheet_name='Sheet1')
    df= df.iloc[7:,:]
    df = df[df['Unnamed: 2']=='000']
    df.reset_index(drop=True, inplace=True)
    state =  df.loc[0, 'Unnamed: 1']
    
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='5-9']['Unnamed: 6'].values[0], \
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='5-9']['Unnamed: 7'].values[0])
                )

    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='10-14']['Unnamed: 6'].values[0], \
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='10-14']['Unnamed: 7'].values[0])
                )
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='15-19']['Unnamed: 6'].values[0], \
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='15-19']['Unnamed: 7'].values[0])
                )
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='20-24']['Unnamed: 6'].values[0], \
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='20-24']['Unnamed: 7'].values[0])
                )
        
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='25-29']['Unnamed: 6'].values[0], \
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='25-29']['Unnamed: 7'].values[0])
                )
        
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='30-34']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='35-39']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='40-44']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='45-49']['Unnamed: 6'].values[0], 
               
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='30-34']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='35-39']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='40-44']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='45-49']['Unnamed: 7'].values[0]
               
               ))
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='50-54']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='55-59']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='60-64']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='65-69']['Unnamed: 6'].values[0],
               
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='50-54']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='55-59']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='60-64']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='65-69']['Unnamed: 7'].values[0]
               ))
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='70-74']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='75-79']['Unnamed: 6'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='80+']['Unnamed: 6'].values[0],
               
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='70-74']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='75-79']['Unnamed: 7'].values[0]+\
               df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='80+']['Unnamed: 7'].values[0]
               ))
    
    lst.append(createDict(df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='Age not stated']['Unnamed: 6'].values[0],
                          df[df['C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ']=='Age not stated']['Unnamed: 7'].values[0])
               )

    total_dict[state] = lst
    
    


df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']!='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2','Unnamed: 4','Unnamed: 9', 'Unnamed: 10', 'Unnamed: 6', 'Unnamed: 7' ]]

df1.columns = ['State-Code', 'State-Name','Age-group','3+Males', '3+Females', '2Males', '2Females']

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
    t['age-group-males'] = tmp[tmp['3+_pct_males']==maxx_males]['Age-group'].values[0]
    t['ratio-of-3-males'] = maxx_males
    t['age-group-females'] = tmp[tmp['3+_pct_females']==maxx_females]['Age-group'].values[0]
    t['ratio-of-3-females'] = maxx_females
    out.append(t)
    
df = pd.DataFrame(out)

df.columns = ['state/ut', 'age-group-males', 'ratio-males', 'age-group-females','ratio-females']
df.sort_values('state/ut', inplace=True)
df.to_csv('output/age-gender-a.csv', index=False)











df1['1Males'] = df1['Total_Males'] - df1['2Males'] 
df1['1Females'] = df1['Total_Females'] - df1['2Females'] 


df1['2Males'] =   df1['2Males']  - df1['3+Males']
df1['2Females'] = df1['2Females']  - df1['3+Females']

df1['2_pct_males'] = df1['2Males']/df1['Total_Males']
df1['2_pct_females'] = df1['2Females']/df1['Total_Females']

#.drop(['State-Name', '3+', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx_males = tmp['2_pct_males'].max()
    maxx_females = tmp['2_pct_females'].max()
    t['state/ut'] = state
    t['age-group-males'] = tmp[tmp['2_pct_males']==maxx_males]['Age-group'].values[0]
    t['ratio-of-2-males'] = maxx_males
    t['age-group-females'] = tmp[tmp['2_pct_females']==maxx_females]['Age-group'].values[0]
    t['ratio-of-2-females'] = maxx_females
    out.append(t)
    
df = pd.DataFrame(out)
df.columns = ['state/ut', 'age-group-males', 'ratio-males', 'age-group-females','ratio-females']
df.sort_values('state/ut', inplace=True)
df.to_csv('output/age-gender-b.csv', index=False)














df1['1_pct_males'] = df1['1Males']/df1['Total_Males']
df1['1_pct_females'] = df1['1Females']/df1['Total_Females']

#.drop(['State-Name', '3+', 'Total'], axis = 1, inplace=True)

#df1 = df1.groupby(['State-Code','Age-group']).agg('max'
df1.reset_index(drop=True, inplace=True)


out = []
for state in all_states:
    t = {}
    tmp = df1[df1['State-Code']==state]
    tmp.reset_index(drop=True, inplace = True)
    maxx_males = tmp['1_pct_males'].max()
    maxx_females = tmp['1_pct_females'].max()
    t['state/ut'] = state
    t['age-group-males'] = tmp[tmp['1_pct_males']==maxx_males]['Age-group'].values[0]
    t['ratio-of-1-males'] = maxx_males
    t['age-group-females'] = tmp[tmp['1_pct_females']==maxx_females]['Age-group'].values[0]
    t['ratio-of-1-females'] = maxx_females
    out.append(t)
    
df = pd.DataFrame(out)
df.columns = ['state/ut', 'age-group-males', 'ratio-males', 'age-group-females','ratio-females']
df.sort_values('state/ut', inplace=True)
df.to_csv('output/age-gender-c.csv', index=False)

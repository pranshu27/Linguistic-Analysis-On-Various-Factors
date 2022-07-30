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
from scipy import stats


df = pd.read_excel("c14/DDW-0000C-14.xls")
df.columns = ['Table_name','State_code','Dist_code','State_Name','Age-group','Total_Persons','Total_Males','Total_Females','Rural Population','Rural_Males','Rural_Females','Urban Population','Urban_Males','Urban_Females']
df = df[6:]
df = df[df['Dist_code']=='000']
df.reset_index(drop=True,inplace=True)
df.fillna(0,inplace=True)    
df = df[(df['Age-group']=='All ages')]
df = df[['State_code','Urban Population','Rural Population']]
# df.reset_index(drop=True, inplace=True)
final =df.copy()
final.reset_index(drop=True, inplace=True)

df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[((df1['Unnamed: 3']=='Rural') | (df1['Unnamed: 3']=='Urban')) & (df1['Unnamed: 4']=='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2',  'Unnamed: 3','Unnamed: 8', 'Unnamed: 5']]

df1.columns = ['State-Code', 'State-Name','Area','3+', '2']

df1.reset_index(drop=True, inplace=True)



for i in range(len(df1)):
    if df1.loc[i, 'Area']=='Rural':
    
        df1.loc[i,'Total'] = final[final['State_code']==df1.loc[i, 'State-Code']]['Rural Population'].values[0]
    else:
        df1.loc[i,'Total'] = final[final['State_code']==df1.loc[i, 'State-Code']]['Urban Population'].values[0]

    
df1['1'] = df1['Total'] - df1['2'] 
df1['2'] = df1['2'] - df1['3+'] 
    
out = []
all_states = set(df1['State-Name'])

for state in all_states:
    tmp_df = df1[df1['State-Name']==state]
    tmp_df.reset_index(drop=True, inplace=True)

    tmp = {}
    for i in range(len(tmp_df)):
        
        tmp['state/ut'] = tmp_df.loc[i, 'State-Code']
        tmp['State-Name'] = tmp_df.loc[i, 'State-Name']
        if tmp_df.loc[i, 'Area']=='Rural':
            tmp['rural-1'] = tmp_df.loc[i, '1']
            tmp['rural-2'] = tmp_df.loc[i, '2']
            tmp['rural-3+'] = tmp_df.loc[i, '3+']
            tmp['rural-total'] = tmp_df.loc[i, 'Total']
            tmp['rural-percentage-one'] = tmp_df.loc[i, '1']*100/ tmp_df.loc[i, 'Total']
            tmp['rural-percentage-two'] = tmp_df.loc[i, '2']*100/ tmp_df.loc[i, 'Total']
            tmp['rural-percentage-three'] = tmp_df.loc[i, '3+']*100/ tmp_df.loc[i, 'Total']
        else:
            tmp['urban-1'] = tmp_df.loc[i, '1']
            tmp['urban-2'] = tmp_df.loc[i, '2']
            tmp['urban-3+'] = tmp_df.loc[i, '3+']
            tmp['urban-total'] = tmp_df.loc[i, 'Total']
            tmp['urban-percentage-one'] = tmp_df.loc[i, '1']*100/ tmp_df.loc[i, 'Total']
            tmp['urban-percentage-two'] = tmp_df.loc[i, '2']*100/ tmp_df.loc[i, 'Total']
            tmp['urban-percentage-three'] = tmp_df.loc[i, '3+']*100/ tmp_df.loc[i, 'Total']
    out.append(tmp)

df1 = pd.DataFrame(out)

df1['3+ratio'] = df1['urban-3+']/df1['rural-3+']
df1['2ratio'] = df1['urban-2']/df1['rural-2']
df1['1ratio'] = df1['urban-1']/df1['rural-1']


df1['popratio'] =df1['urban-total']/ df1['rural-total']

df1.reset_index(drop=True, inplace = True)



for i in range(len(df1)):
    tmp = []
    tmp.append(df1.loc[i,'1ratio'])
    tmp.append(df1.loc[i,'2ratio'])
    tmp.append(df1.loc[i,'3+ratio'])
    
    mean = float(df1.loc[i,'popratio'])
    _, pval = stats.ttest_1samp(tmp, mean)
    #break
    df1.loc[i, 'pvalue'] = pval
    
df1.sort_values('state/ut', inplace = True)

df1 = df1[['state/ut', 'rural-percentage-one', 'rural-percentage-two',  'rural-percentage-three', 'urban-percentage-one', 'urban-percentage-two', 'urban-percentage-three', 'pvalue']]

df_one = df1[['state/ut', 'urban-percentage-one', 'rural-percentage-one', 'pvalue']]
df_two = df1[['state/ut', 'urban-percentage-two','rural-percentage-two', 'pvalue']]
df_three = df1[['state/ut', 'urban-percentage-three', 'rural-percentage-three', 'pvalue']]


df_one.columns = ['state-code', 'urban-percentage', 'rural-percentage', 'p-value']
df_two.columns = ['state-code', 'urban-percentage', 'rural-percentage', 'p-value']
df_three.columns = ['state-code', 'urban-percentage', 'rural-percentage', 'p-value']


df_one.to_csv('output/geography-india-a.csv', index=False)
df_two.to_csv('output/geography-india-b.csv', index=False)
df_three.to_csv('output/geography-india-c.csv', index=False)


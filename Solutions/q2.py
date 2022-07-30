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

total_dict = {}
for f in os.listdir('c17'):
    #print(f)
    df = pd.read_excel('c17/'+f, sheet_name='Sheet1')
    
    df= df.iloc[5:,:]
    df.reset_index(drop=True, inplace=True)
    df.fillna(0, inplace = True)
    state =  df.loc[0, 'Unnamed: 1']
    df['Unnamed: 5'] = df['Unnamed: 5'].astype(int)
    df['Unnamed: 6'] = df['Unnamed: 6'].astype(int)
    
 
    m = df['Unnamed: 5'].sum()
    f = df['Unnamed: 6'].sum()
    
    total_dict[state] = [m,f]
    

df1 = pd.read_excel('DDW-C18-0000.xlsx', sheet_name='Sheet1')
df1= df1.iloc[5:,:]

df1 = df1[(df1['Unnamed: 3']=='Total') & (df1['Unnamed: 4']=='Total')]

df1.columns

df1 = df1[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX', 'Unnamed: 2','Unnamed: 9', 'Unnamed: 10', 'Unnamed: 6', 'Unnamed: 7' ]]

df1.columns = ['State-Code', 'State-Name','3+Males', '3+Females', '2Males', '2Females']

df1.reset_index(drop=True, inplace=True)

for i in range(len(df1)):

    df1.loc[i,'Total_Males'] = total_dict[df1.loc[i, 'State-Name']][0]
    df1.loc[i,'Total_Females'] = total_dict[df1.loc[i, 'State-Name']][1]
#df.drop([0,4], axis = 0, inplace = True)
#df1 = df1[df1['State-Name']!='INDIA']

df1['1Males'] = df1['Total_Males'] - df1['2Males'] 
df1['1Females'] = df1['Total_Females'] - df1['2Females'] 

df1['male-percent-one'] = df1['1Males']*100/df1['Total_Males']
df1['female-percent-one'] = df1['1Females']*100/df1['Total_Females']


df1['2Males'] =   df1['2Males']  - df1['3+Males']
df1['2Females'] = df1['2Females']  - df1['3+Females']

df1['male-percent-two'] = df1['2Males']*100/df1['Total_Males']
df1['female-percent-two'] = df1['2Females']*100/df1['Total_Females']


df1['male-percent-three'] = df1['3+Males']*100/df1['Total_Males']
df1['female-percent-three'] = df1['3+Females']*100/df1['Total_Females']



df1.reset_index(drop=True, inplace = True)




df1['3+ratio'] = df1['3+Males']/df1['3+Females']
df1['2ratio'] = df1['2Males']/df1['2Females']
df1['1ratio'] = df1['1Males']/df1['1Females']


df1['popratio'] = df1['Total_Males']/df1['Total_Females']

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



df1.columns

df1.drop(['State-Name', '3+Males', '3+Females',
       '2Males', '2Females', 'Total_Males', 'Total_Females', '1Males',
       '1Females', '3+ratio', '2ratio', '1ratio', 'popratio'], axis = 1, inplace=True)

df1.columns = ['state-code', 'male-percent-one', 'female-percent-one', \
       'male-percent-two', 'female-percent-two', 'male-percent-three', \
       'female-percent-three', 'pvalue']

#df1 = df1[['state-code', 'male-percent-one', 'male-percent-two', 'male-percent-three',\
          #'female-percent-one', 'female-percent-two', 'female-percent-three', 'pvalue']]
# =============================================================================
# df1['Male_pct'] = df1['3+Males']*100/df1['Total_Males']
# df1['Female_pct'] = df1['3+Females']*100/df1['Total_Females']
# df1['m/f'] = np.abs(df1['Male_pct']/df1['Female_pct'])
# df1.reset_index(drop=True, inplace=True)
# 
# 
# df1.drop(['State-Name', '3+Males', '3+Females', 'Total_Males',
#        'Total_Females' ], axis = 1, inplace=True)
# 
# df1.columns = ['State-Code','male-percentage', 'female-percentage', 'm/f']
# 
# 
# =============================================================================

df_one = df1[['state-code', 'male-percent-one', 'female-percent-one','pvalue']]
df_two = df1[['state-code', 'male-percent-two', 'female-percent-two','pvalue']]
df_three = df1[['state-code', 'male-percent-three', 'female-percent-three','pvalue']]

df_one.columns = ['state-code', 'male-percentage', 'female-percentage','p-value']
df_two.columns = ['state-code', 'male-percentage', 'female-percentage','p-value']
df_three.columns = ['state-code', 'male-percentage', 'female-percentage','p-value']


df_one.to_csv('output/gender-india-a.csv', index=False)
df_two.to_csv('output/gender-india-b.csv', index=False)
df_three.to_csv('output/gender-india-c.csv', index=False)


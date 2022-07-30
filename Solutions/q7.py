
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 11:20:24 2021

@author: pranshu
"""
'''
1	JAMMU & KASHMIR
2	HIMACHAL PRADESH
3	PUNJAB
4	CHANDIGARH
5	UTTARAKHAND
6	HARYANA
7	NCT OF DELHI
8	RAJASTHAN
9	UTTAR PRADESH
10	BIHAR
11	SIKKIM
12	ARUNACHAL PRADESH
13	NAGALAND
14	MANIPUR
15	MIZORAM
16	TRIPURA
17	MEGHALAYA
18	ASSAM
19	WEST BENGAL
20	JHARKHAND
21	ODISHA
22	CHHATTISGARH
23	MADHYA PRADESH
24	GUJARAT
25	DAMAN & DIU
26	DADRA & NAGAR HAVELI
27	MAHARASHTRA
28	ANDHRA PRADESH
29	KARNATAKA
30	GOA
31	LAKSHADWEEP
32	KERALA
33	TAMIL NADU
34	PUDUCHERRY
35	ANDAMAN & NICOBAR ISLANDS

 North: JK, Ladakh, PN, HP, HR, UK, Delhi, Chandigarh
• West: RJ, GJ, MH, Goa, Dadra & Nagar Haveli, Daman & Diu
• Central: MP, UP, CG
• East: BH, WB, OR, JH
• South: KT, TG, AP, TN, KL, Lakshadweep, Puducherry
• North-East: AS, SK, MG, TR, AR, MN, NG, MZ, Andaman & Nicobar

'''
import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

north = ['01', '04', '07', '05', '06', '02', '03']
#north = ['01', '02']
west = ['08', '24', '27', '30', '26', '25']
central = ['23', '09', '22']
east = ['10', '19', '21', '20']
south = ['29', '33', '28', '32', '31', '34']
north_east = ['18', '11', '17', '16', '12','14','13','15','35']

out = []
regions = {
    'North': north, 
    'West':west, 
    'Central':central, 
    'East':east, 
    'South':south, 
    'North-East':north_east}

for region in regions.keys():
    tmp = {}
    lang_dict = {}
    #print(region)
    for f in os.listdir('c17'):
        
        if f.split('.')[0].split('-')[2][0:2] in regions[region]:
            
            #print(f)
            df = pd.read_excel('c17/'+f, sheet_name='Sheet1')
            df = df.iloc[5:, :]
            df.reset_index(drop=True, inplace=True)
            df.fillna(-1, inplace = True)
            df['Unnamed: 4'] = df['Unnamed: 4'].astype(int);
            df['Unnamed: 9'] = df['Unnamed: 9'].astype(int);
            df['Unnamed: 14'] = df['Unnamed: 14'].astype(int);
            
 
        
            for i in range(len(df)):
                
                if df.loc[i, 'Unnamed: 3'] != -1:
                    if df.loc[i, 'Unnamed: 3'] not in lang_dict.keys():
                        #print('daala')
                        lang_dict[df.loc[i, 'Unnamed: 3']] = df.loc[i, 'Unnamed: 4']
                    else:
                       # print('added')
                        lang_dict[df.loc[i, 'Unnamed: 3']] += df.loc[i, 'Unnamed: 4']
            
            #df.reset_index(drop=True, inplace=True)
            for i in range(len(df)):
                
                if df.loc[i, 'Unnamed: 8'] != -1:
                    if df.loc[i, 'Unnamed: 8'] not in lang_dict.keys():
                        lang_dict[df.loc[i, 'Unnamed: 8']] = df.loc[i, 'Unnamed: 9']
                    else:
                        #print('added')
                        lang_dict[df.loc[i, 'Unnamed: 8']] += df.loc[i, 'Unnamed: 9']
                
                
            #df.reset_index(drop=True, inplace=True)
            for i in range(len(df)):
                
                if df.loc[i, 'Unnamed: 13'] != -1:
                    if df.loc[i, 'Unnamed: 13'] not in lang_dict.keys():
                        lang_dict[df.loc[i, 'Unnamed: 13']] = df.loc[i, 'Unnamed: 14']
                    else:
                        lang_dict[df.loc[i, 'Unnamed: 13']] += df.loc[i, 'Unnamed: 14']

            
    top3=sorted(lang_dict, key=lang_dict.get, reverse=True)[:3]
    #print(top3)
    tmp['region'] = region
    tmp['language-1'] = top3[0]
    tmp['language-2'] = top3[1]
    tmp['language-3'] = top3[2]


    out.append(tmp)
    

out = pd.DataFrame(out)
out.sort_values('region', inplace = True)
out.to_csv('output/region-india-b.csv', index=False)




























out = []
for region in regions.keys():
    tmp = {}
    lang_dict = {}
    #print(region)
    for f in os.listdir('c17'):
        
        if f.split('.')[0].split('-')[2][0:2] in regions[region]:
            
            #print(f)
            df = pd.read_excel('c17/'+f, sheet_name='Sheet1')
            df = df.iloc[5:, :]
            df.reset_index(drop=True, inplace=True)
            df.fillna(-1, inplace = True)
            df['Unnamed: 4'] = df['Unnamed: 4'].astype(int);
            df['Unnamed: 9'] = df['Unnamed: 9'].astype(int);
            df['Unnamed: 14'] = df['Unnamed: 14'].astype(int);
            
 
        
            for i in range(len(df)):
                
                if df.loc[i, 'Unnamed: 3'] != -1:
                    if df.loc[i, 'Unnamed: 3'] not in lang_dict.keys():
                        #print('daala')
                        lang_dict[df.loc[i, 'Unnamed: 3']] = df.loc[i, 'Unnamed: 4']
                    else:
                       # print('added')
                        lang_dict[df.loc[i, 'Unnamed: 3']] += df.loc[i, 'Unnamed: 4']


            
    top3=sorted(lang_dict, key=lang_dict.get, reverse=True)[:3]
    #print(top3)
    tmp['region'] = region
    tmp['language-1'] = top3[0]
    tmp['language-2'] = top3[1]
    tmp['language-3'] = top3[2]


    out.append(tmp)
    

out = pd.DataFrame(out)
out.sort_values('region', inplace = True)
out.to_csv('output/region-india-a.csv', index=False)




#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:54:49 2016

@author: cz
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pyzipcode import ZipCodeDatabase

dirLoc = '/home/cz/ML/Incubator/Project/'

file14 = 'zipcode2014/14zpallagi.csv'
"2nd column is 'zipcode', column 14 'A00100' is gross income. Each zipcode has 6 classes (in column 3 'agi_stub'), need to sum up."
data14 = pd.read_csv(dirLoc+file14,header=0,usecols=[2, 3, 14])
data14 = data14.pivot_table(values='A00100',index='zipcode',columns='agi_stub',aggfunc='sum').sum(axis=1)
index=(data14.index.values<99999)&(data14.index.values>0)
data14 = data14[index]

file09= '2009zipcode/09zpallagi.csv'
"2nd column is 'zipcode',  column 9 'A00100' is gross income. Each zipcode has 6 classes (in column 3 'agi_stub'), need to sum up."
data09 = pd.read_csv(dirLoc+file09,header=0,usecols=[2, 3, 9])
data09 = data09.pivot_table(values='A00100',index='zipcode',columns='agi_stub',aggfunc='sum').sum(axis=1)
index=(data09.index.values<99999)&(data09.index.values>0)
data09 = data09[index]

ratio = data14.div(data09,axis=0).sort_values(ascending=False).dropna()

number = 10
"""
y = list(ratio.values[0:number])
y.extend(list(ratio.values[-number:]))
xticks = []
zcdb = ZipCodeDatabase()
for i in ratio.index.values[0:number]:
    print(i)
    myzip = str(i).zfill(5)
    xticks.append(myzip+'_'+zcdb[myzip].state)
for i in ratio.index.values[-number:]:
    print(i)
    myzip = str(i).zfill(5)
    xticks.append(myzip+'_'+zcdb[myzip].state)
plt.figure(figsize=(12,4))
plt.bar(range(2*number),y, align='center', alpha=0.5)
plt.xticks(range(2*number),xticks)
plt.show()
"""
y = list(ratio.values[0:number])
xticks = []
zcdb = ZipCodeDatabase()
for i in ratio.index.values[0:number]:
    print(i)
    myzip = str(i).zfill(5)
    xticks.append(myzip+'_'+zcdb[myzip].state)
    
#%%
matplotlib.rcParams.update({'font.size': 22})
plt.figure(figsize=(24,12))
plt.bar(range(number),y, align='center',alpha=0.3)
plt.xlim(-1,number)
plt.xticks(range(number),xticks)
plt.xlabel('zipcode+state')
plt.ylabel('Wealth growth rate from 2009 to 2014')
plt.title('Top '+str(number)+' Communities in Wealth Growth')
plt.savefig('TopGrowth')
plt.show()
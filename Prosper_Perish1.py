#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:54:34 2016

@author: cz
"""

"""
09
3, 
"""
import pandas as pd
import matplotlib.pyplot as plt

dirLoc = '/home/cz/ML/Incubator/Project/'
class1 = []
class2 = []
class3 = []
class4 = []
"For unknown reason, year 2011 is outliner. To see year 2011, change range(9,11) to range(9,12)"
for i in range(9,11):
    i_str = str(i).zfill(2)
    folder = '20' + i_str + 'zipcode/'
    fileName = i_str + 'zpallagi.csv'
    fileLoc = dirLoc + folder + fileName
    """
    agi_stub divideds taxplayer into 6 categories based on their income.
    I will group them into 4 Classes: class 1 {cat 1&2} below 50K, class 2 {cat 3&4} 50~100K, class 3 {cat 5} 100~200K, class 4 {cat 6} above 200K
    A00300, A00600, A01000 is income by different kinds of risky investment.
    """
    data = pd.read_csv(fileLoc,header=0,usecols=['agi_stub', 'N1', 'A00300', 'A00600', 'A01000'])
    data[['A00300', 'A00600', 'A01000']] = data[['A00300', 'A00600', 'A01000']].div(data['N1'],axis=0)
    data = data[['agi_stub','A00300', 'A00600', 'A01000']]
    data = data.pivot_table(values=['A00300', 'A00600', 'A01000'],index='agi_stub',aggfunc='mean').sum(axis=1)
    class1.append( float(data[0:1])+float(data[1:2]) )
    class2.append( float(data[2:3])+float(data[3:4]) )
    class3.append( float(data[4:5]) )
    class4.append( float(data[5:6]) )

i_str = str(12).zfill(2)
folder = '20' + i_str + 'zipcode/'
fileName = i_str + 'zpallagi.csv'
fileLoc = dirLoc + folder + fileName
data = pd.read_csv(fileLoc,header=0,usecols=['AGI_STUB', 'N1', 'A00300', 'A00600', 'A01000'])
data[['A00300', 'A00600', 'A01000']] = data[['A00300', 'A00600', 'A01000']].div(data['N1'],axis=0)
data = data[['AGI_STUB','A00300', 'A00600', 'A01000']]
data = data.pivot_table(values=['A00300', 'A00600', 'A01000'],index='AGI_STUB',aggfunc='mean').sum(axis=1)
class1.append( float(data[0:1])+float(data[1:2]) )
class2.append( float(data[2:3])+float(data[3:4]) )
class3.append( float(data[4:5]) )
class4.append( float(data[5:6]) )    

for i in range(13,15):
    i_str = str(i).zfill(2)
    folder = 'zipcode20' + i_str + '/'
    fileName = i_str + 'zpallagi.csv'
    fileLoc = dirLoc + folder + fileName
    data = pd.read_csv(fileLoc,header=0,usecols=['agi_stub','N1', 'A00300', 'A00600', 'A01000'])
    data[['A00300', 'A00600', 'A01000']] = data[['A00300', 'A00600', 'A01000']].div(data['N1'],axis=0)
    data = data[['agi_stub','A00300', 'A00600', 'A01000']]
    data = data.pivot_table(values=['A00300', 'A00600', 'A01000'],index='agi_stub',aggfunc='mean').sum(axis=1)
    class1.append( float(data[0:1])+float(data[1:2]) )
    class2.append( float(data[2:3])+float(data[3:4]) )
    class3.append( float(data[4:5]) )
    class4.append( float(data[5:6]) )
"unit is K dollar, convert to dollar"
"""
class1 = [x*1000 for x in class1]
class2 = [x*1000 for x in class2]
class3 = [x*1000 for x in class3]
class4 = [x*1000 for x in class4]
"""
#%%
plt.figure(figsize=(12,6))
"For unknown reason, year 2011 is outliner. To see year 2011, add 2011 to time."
time=[2009,2010,2012,2013,2014]
time_str = [str(x) for x in time]
plt.plot(time,class1,time,class2,time,class3,time,class4)
plt.yscale('log')
plt.xlim(2008.7,2014.3)
plt.ylim(0,200)
plt.xticks(time,time_str)
plt.xlabel('year')
plt.ylabel('Passive Investment Income')
plt.legend(['Total Income: < 50K','Total Income: 50K ~ 100K','Total Income: 100K ~ 200K','Total Income: > 200K'],loc=7)
plt.title('Passive Investment Income of Different Class after Financial Crisis 2008')
plt.savefig('RiskyInvestmentIncome')
plt.show()
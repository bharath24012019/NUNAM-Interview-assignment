#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Install xlrd and openpyxl using pip command before executing the file

import pandas as pd
import numpy as np


# In[3]:


#Using Pandas dataframes to read 'detail.csv' , 'detailVol.csv' and 'detailTemp.csv'
#df1 ----> detail.csv
#df2 ----> detailVol.csv
#df3 ----> detailTemp.csv

df1 = pd.read_csv('detail.csv')
df2 = pd.read_csv('detailVol.csv')
df3 = pd.read_csv('detailTemp.csv')


# In[11]:


#The 'Absolute Time' and 'Realtime' objects are converted to datatime64 in df1, df2 and df3

df1['Absolute Time'] = df1['Absolute Time'].astype('datetime64')
df2['Realtime'] = df2['Realtime'].astype('datetime64')
df3['Realtime'] = df3['Realtime'].astype('datetime64')


# In[13]:


#df4, df5 and df6 are downsampled versions of df1, df2 and df3 respectively

df4 = df1.resample('60s', on='Absolute Time').first()
df5 = df2.resample('60s', on='Realtime').first()
df6 = df3.resample('60s', on='Realtime').first()


# In[17]:


#df4 stored as 'detailDownsampled.csv'
#df5 stored as 'detailVolDownsampled.csv'
#df6 stored as 'detailTempDownsampled.csv'

df4.to_csv('detailDownsampled.csv')
df5.to_csv('detailVolDownsampled.csv')
df6.to_csv('detailTempDownsampled.csv')


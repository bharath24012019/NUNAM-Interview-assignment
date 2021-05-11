#!/usr/bin/env python
# coding: utf-8

# In[64]:


#Install xlrd and openpyxl using pip command before executing the file

import pandas as pd
import numpy as np


# In[65]:


#df1,df2,df3,df4,df5,df6 and df7 are dataframes that contain the sheets related to Detail_67 

df1 = pd.read_excel('data.xlsx','Detail_67_1_1')
df2 = pd.read_excel('data.xlsx','Detail_67_1_1_1')
df3 = pd.read_excel('data.xlsx','Detail_67_1_1_2')
df4 = pd.read_excel('data.xlsx','Detail_67_1_1_3')
df5 = pd.read_excel('data.xlsx','Detail_67_1_1_4')
df6 = pd.read_excel('data.xlsx','Detail_67_1_1_5')
df7 = pd.read_excel('data.xlsx','Detail_67_1_1_6')


# In[66]:


#df8 is formed by appending df1 - df7
#df_list is a list of dataframes df1 - df7

df8 = pd.DataFrame()
df_list = [df1,df2,df3,df4,df5,df6,df7]
for dataframe in df_list:
    df8 = df8.append(dataframe, ignore_index = True)


# In[67]:


#df9,df10,df11,df12,df13,df14 and df15 are dataframes that contain the sheets related to DetailVol_67 

df9 = pd.read_excel('data.xlsx','DetailVol_67_1_1')
df10 = pd.read_excel('data.xlsx','DetailVol_67_1_1_1')
df11 = pd.read_excel('data.xlsx','DetailVol_67_1_1_2')
df12 = pd.read_excel('data.xlsx','DetailVol_67_1_1_3')
df13 = pd.read_excel('data.xlsx','DetailVol_67_1_1_4')
df14 = pd.read_excel('data.xlsx','DetailVol_67_1_1_5')
df15 = pd.read_excel('data.xlsx','DetailVol_67_1_1_6')


# In[68]:


#df16 is formed by appending df9 - df15
#df_list_1 is a list of dataframes df9 - df15

df16 = pd.DataFrame()
df_list_1 = [df9,df10,df11,df12,df13,df14,df15]
for dataframe in df_list_1:
    df16 = df16.append(dataframe, ignore_index = True)


# In[69]:


#df17,df18,df19,df20,df21,df22 and df23 are dataframes that contain the sheets related to DetailTemp_67 

df17 = pd.read_excel('data.xlsx','DetailTemp_67_1_1')
df18 = pd.read_excel('data.xlsx','DetailTemp_67_1_1_1')
df19 = pd.read_excel('data.xlsx','DetailTemp_67_1_1_2')
df20 = pd.read_excel('data_1.xlsx','DetailTemp_67_1_1_3')
df21 = pd.read_excel('data_1.xlsx','DetailTemp_67_1_1_4')
df22 = pd.read_excel('data_1.xlsx','DetailTemp_67_1_1_5')
df23 = pd.read_excel('data_1.xlsx','DetailTemp_67_1_1_6')


# In[70]:


#df24 is formed by appending df17 - df23
#df_list_2 is a list of dataframes df17 - df23

df24 = pd.DataFrame()
df_list_2 = [df17,df18,df19,df20,df21,df22,df23]
for dataframe in df_list_2:
    df24 = df24.append(dataframe, ignore_index = True)


# In[74]:


#df8 is saved as detail.csv
#df16 is saved as detailVol.csv
#df24 is saved as detailTemp.csv

df8.to_csv('detail.csv')
df16.to_csv('detailVol.csv')
df24.to_csv('detailTemp.csv')


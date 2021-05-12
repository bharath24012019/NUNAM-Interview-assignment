#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Install xlrd and openpyxl using pip command before executing the file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from scipy.signal import butter,filtfilt


# In[2]:


#Plot of 'Auxiliary channel TU1 U(V)' before filtering

df1 = pd.read_csv('detailVolDownsampled.csv')
df1.plot(y='Auxiliary channel TU1 U(V)', figsize=(25,4))


# In[3]:


#Removed all package except 'Auxiliary channel TU1 U(V)' and 'Realtime
'
df3 = df1
df3 = df3.drop(columns=['Unnamed: 0','Record ID','Step Name','Relative Time(h:min:s.ms)','Realtime.1','Gap of Voltage'])


# In[4]:


#Noise reduction and data visualization

import scipy.signal as signal
sos = signal.butter(20, 10000, 'lp', fs=250000, output='sos')
filtered = signal.sosfiltfilt(sos, df3['Auxiliary channel TU1 U(V)'])
df4 = df3
df4['Auxiliary channel TU1 U(V)'] = filtered
df4.plot(y='Auxiliary channel TU1 U(V)', figsize=(15,15))
filtered


# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:43:20 2018

@author: Daante
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing test and train dataser

df_test = pd.read_csv('test.csv', header = None)
df_train = pd.read_csv('train.csv', header = None)
print(df_train.describe())
print(df_test.head(20))
#Removiong the empty values
from sklearn.preprocessing import Imputer
df_train.isnull().any()
df_test.isnull().any()
df_train.isnull().sum()
df_test.isnull().sum()
df_test = df_test.drop(df_test.columns[[9]], axis = 1)
df_train2
df_train = df_train.drop(df_train.columns[[10]], axis = 1)
imputer = Imputer(missing_values= 'nan', strategy= 'most_frequent' , axis= 0)
train_values = df_train.values
test_values = df_test.values

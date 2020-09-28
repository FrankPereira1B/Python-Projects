# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:14:33 2020

@author: pereifr
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:57:52 2020

@author: pereifr
"""

# Importing Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# Importing the dataset

dataset = pd.read_csv("EURUSD.csv")


# converting Date Object to Datetime

dataset['Date'] = pd.to_datetime(dataset['Date'].str.strip(), format='%b %d, %Y')


# Adding new columns for SMA 20 and SMA 50

dataset['MA 20'] = dataset['Price'].rolling(window=20).mean()
dataset['MA 50'] = dataset['Price'].rolling(window=50).mean()

#Trading Logic - If SMA 20 crosses SMA 50 then Buy provided SMA 20 is lower than SMA 50 the previous day

dataset['Previous MA 20'] = dataset['MA 20'].shift(1)
dataset['Previous MA 50'] = dataset['MA 50'].shift(1)

dataset['Trading Signal'] = np.where((dataset['MA 20'] > dataset['MA 50']) & (dataset['Previous MA 20'] < dataset['Previous MA 50']), "BUY", 
                                     
                                     (np.where((dataset['MA 20'] < dataset['MA 50']) & (dataset['Previous MA 20'] > dataset['Previous MA 50']), "SELL", "")))

dataset['Trading Price'] = np.where(dataset['Trading Signal']=="BUY", dataset['Price'],
                                    (np.where(dataset['Trading Signal']=="SELL", dataset['Price'], "" )))


dataset['Trading Price'] = dataset['Trading Price'].replace(r'^\s*$', np.NaN, regex=True)

dataset['Trade Closing Price'] = dataset['Trading Price']

dataset['Trade Closing Price'] = dataset['Trading Price'].shift(1).fillna(method='ffill')

dataset['Trading Price'] = dataset['Trading Price'].replace(np.nan,0)

dataset['Trade Closing Price'] = dataset['Trade Closing Price'].replace(np.nan,0)

dataset['Trading Price'] = dataset['Trading Price'].apply(pd.to_numeric)   
 
dataset['Trade Closing Price'] = dataset['Trade Closing Price'].apply(pd.to_numeric)     

dataset['Difference'] = np.where(dataset['Trading Signal'] == "BUY", dataset['Trade Closing Price'] - dataset['Trading Price'],
                                 (np.where(dataset['Trading Signal'] == "SELL", dataset['Trading Price'] - dataset['Trade Closing Price'], "")))


dataset['Returns'] = np.where((dataset['Trading Price'] != 0) & (dataset['Trade Closing Price'] == 0), 0, 
                              (np.where(dataset['Trading Price'] != 0, dataset['Difference'], "")))

dataset['Returns'] = dataset['Returns'].apply(pd.to_numeric)   

dataset['Returns'] = dataset['Returns'].replace(np.nan,0)

dataset['Pips'] = dataset['Returns']*10000

Pips = round(dataset['Pips'].sum(),0)

Total_Buy_Orders = (dataset['Trading Signal'] == "BUY").sum()

Total_Sell_Orders = (dataset['Trading Signal'] == "SELL").sum()

Total_Buy_Pips = dataset[dataset['Trading Signal']=="BUY"]['Returns'].sum()*10000

Total_Sell_Pips = dataset[dataset['Trading Signal']=="SELL"]['Returns'].sum()*10000


#======================================================
# Integrating Machine Learning using Logistic Regression

dataset['Trading Signal'] = np.where(dataset['Trading Signal'] == "BUY", 0,
                                     (np.where(dataset['Trading Signal'] =="SELL", 1, "")))



x = dataset.iloc[:, 1:3].values
y = dataset.iloc[:, 9:10].values


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))
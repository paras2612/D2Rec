# -*- coding: utf-8 -*-
"""TestGenerator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EsmYvuWKdbzQJxlLc-QN0NuL5u6V737r
"""

import pandas as pd

ratings = pd.read_csv("/content/drive/MyDrive/Copy of Epinions/Data-final/ratings_data.csv")
ratings = ratings[['userId', 'productId', 'rating']]

from sklearn.model_selection import train_test_split


train,test = train_test_split(ratings,test_size=0.4,random_state=1)

train

test.to_csv("/content/drive/MyDrive/Copy of Epinions/testData_Final/ratings_data_test.csv")

train.to_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/ratings_data_train.csv")

test_new = test

x = test_new.groupby("productId")
items = list(x.groups.keys())

import numpy as np
for j in range(2,21):
  for k in range(j//2):
    test = pd.DataFrame()
    train = pd.DataFrame()
    items_sub = []
    for i in items:
      a = x.get_group(i)
      if(len(a)>=j):
        a_sub = a.sample(n=j)
        test = test.append(a_sub, ignore_index=True)
        train = train.append(a[~a.isin(a_sub)].dropna(how = 'all'),ignore_index=True)
      else:
        train = train.append(a,ignore_index=True)
    train.to_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/ratings_data_train_"+str(j)+"_"+str(k)+".csv")
    test.to_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/ratings_data_test_"+str(j)+"_"+str(k)+".csv")
    print("Done for ",k," ",j)

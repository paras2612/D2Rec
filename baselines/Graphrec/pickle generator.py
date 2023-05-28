# -*- coding: utf-8 -*-
"""pickle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oSFbXPJZ6XP206D8Fq8mOwMU4ZbwfXOx
"""

import pandas as pd
import numpy as np

ratings = pd.read_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/ratings_data_train.csv")
data_df = ratings[['userId', 'productId', 'rating']]
ratings

data_df

a = data_df.groupby("userId")

users = list(a.groups.keys())

rating_list = {0.0:0,1.0:1,2.0:2,3.0:3,4.0:4,5.0:5}

user_dict = {}
user_r_dict = {}
for i in range(len(users)):
  items = []
  ratings = []
  for idx,row in a.get_group(users[i]).iterrows():
    items.append(int(row[1]))
    ratings.append(rating_list[row[2]])
  user_dict[int(users[i])]=items
  user_r_dict[int(users[i])]=ratings

b = data_df.groupby("productId")
item = list(b.groups.keys())
item_dict = {}
item_r_dict = {}
for i in range(len(item)):
  user = []
  ratings = []
  for idx,row in b.get_group(item[i]).iterrows():
    user.append(int(row[0]))
    ratings.append(rating_list[row[2]])
  item_dict[int(item[i])]=user
  item_r_dict[int(item[i])]=ratings

len(item_dict)

len(item_r_dict)

train = pd.read_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/ratings_data_train.csv")
train = train[["userId","productId","rating"]]
train_u = []
train_v = []
train_r = []

for idx,row in train.iterrows():
  train_u.append(row[0])
  train_v.append(row[1])
  train_r.append(row[2])

u_train = []
i_train = []
r_train = []
for idx,row in x.iterrows():
  u_train.append(int(row[0]))
  i_train.append(int(row[1]))
  r_train.append(row[2])

import pandas as pd

#trust = pd.read_csv("/content/drive/MyDrive/Copy of Epinions/Data-final/trust_new.csv")

trust = pd.read_csv("/content/drive/MyDrive/Copy of Epinions/Ciao/trust_final.csv")
trust = trust[["from","to","value"]]

adj_lists = {}
c = trust.groupby("from")
user_from = list(c.groups.keys())
for i in range(len(user_from)):
  user = []
  for idx,row in c.get_group(user_from[i]).iterrows():
    user.append(int(row[1]))
  adj_lists[int(user_from[i])]=set(user)

data = [user_dict,user_r_dict,item_dict,item_r_dict,train_u,train_v,train_r,adj_lists,rating_list]

print(len(user_dict))
print(len(user_r_dict))
print(len(item_dict))
print(len(item_r_dict))
print(len(train_u))
print(len(train_v))
print(len(train_r))
print(len(adj_lists))
print(len(rating_list))

import pickle


path = "/content/drive/MyDrive/Copy of Epinions/Ciao/dataset_test.pickle"
with open(path, "wb") as f:
    pickle.dump(data, f)

with open(path, 'rb') as f:
    history_u_lists, history_ur_lists, history_v_lists, history_vr_lists, train_u, train_v, train_r, test_u, test_v, test_r, social_adj_lists, ratings_list = pickle.load(f)
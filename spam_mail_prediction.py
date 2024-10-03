# -*- coding: utf-8 -*-
"""Spam Mail Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPEx6Bbr5X3Yf393AfuAJfAMzDnU9W60
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

raw_mail_data = pd.read_csv('/content/spam_ham_dataset.csv')

print(raw_mail_data)

mail_data=raw_mail_data.where(pd.notnull(raw_mail_data),'')

mail_data.head()

mail_data.shape

mail_data.loc[mail_data['label']=='spam','label']=0
mail_data.loc[mail_data['label']=='ham','label']=1

X=mail_data['text']
Y=mail_data['label']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3)

feature_extraction=TfidfVectorizer(min_df=1,stop_words='english',lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

model = LogisticRegression()

model.fit(X_train_features,Y_train)

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data=accuracy_score(Y_train,prediction_on_training_data)

print('Accuracy on training data : ',accuracy_on_training_data)

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data=accuracy_score(Y_test,prediction_on_test_data)

print('Accuracy on test data : ',accuracy_on_test_data)

input_mail=['cp & l please add a deal in march for 17 , 18 , & 19 th for 5 , 000 a day at hsc gd - . 03']
input_data_features=feature_extraction.transform(input_mail)
prediction=model.predict(input_data_features)
print(prediction)
if (prediction[0]==1):
  print('Ham mail')
else:
  print('Spam mail')


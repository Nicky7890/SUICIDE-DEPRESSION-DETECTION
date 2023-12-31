# -*- coding: utf-8 -*-
"""Suicide-Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQEBLJqtA6YD25sdwg07aBJM3H9fMB09
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import os
for dirname, _, filenames in os.walk('/content/drive/MyDrive/Suicide_Detection.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import ctypes
import os.path
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('/Suicide_Detection.csv')

df = df.fillna('')

df['class'].value_counts()

data = df['class'].value_counts()
names = list(data.keys())
values = list(data.values)

from sklearn.model_selection import train_test_split

df_ml = df

sentences = df['text'].values
y = df_ml['class'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(
sentences, y, test_size=0.20, random_state=1000)


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
X_train

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print('𝐀𝐜𝐜𝐮𝐫𝐚𝐜𝐲 𝐒𝐜𝐨𝐫𝐞:-', score)

def predict_category(s,train=y,model=classifier):
    V=[s]
    vect = CountVectorizer()
    vect.fit(V)
    pr = vectorizer.transform(V)
    pred=model.predict(pr)

    return pred[0]

predict_category('My Girlfriend left me, I do not want to live anymore')
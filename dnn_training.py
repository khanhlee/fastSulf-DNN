# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:57:23 2020

@author: TMU
"""

import numpy as np
import pandas as pd
import keras
from keras.layers import Activation, Dense, BatchNormalization
from keras.models import Sequential
from keras.regularizers import l1
from keras import regularizers
from keras.utils import to_categorical
from sklearn.model_selection import StratifiedKFold
import sys

df = pd.read_csv(sys.argv[1],header=None)

X = df.iloc[:,1:].values
y = df.iloc[:,0].values

epochs = 100
batch_size = 32
learning_rate = 0.01

def build():
    model = Sequential()
    model.add(Dense(100, input_dim = X.shape[1], kernel_regularizer=regularizers.l2(0.01)))
    model.add(Activation('relu'))
    model.add(Dense(200, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(300, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='sigmoid'))
    
    model.compile(loss= 'binary_crossentropy', optimizer= 'adam', metrics=['accuracy'])
    return model

kfold = StratifiedKFold(n_splits = 5, shuffle= True, random_state=42)
cvscores=[]
for train_idx, test_idx in kfold.split(X,y):
    train_X, test_X, train_y, test_y = X[train_idx], X[test_idx], y[train_idx], y[test_idx]
    train_y = to_categorical(train_y)
    test_y = to_categorical(test_y)
    model = build()
    model.fit(train_X, train_y, epochs = epochs, batch_size = batch_size,validation_data = (test_X, test_y), verbose = 0)
    scores = model.evaluate(test_X, test_y, verbose = 0)
    print('%s: %.2f%%'%(model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1]*100)
    
print('Mean accuracy: %.2f%% (S.D.: %.2f%%)'%(np.mean(cvscores), np.std(cvscores)))
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:28:01 2020

@author: TMU
"""
import pandas as pd
import sys

tst_file = sys.argv[1]
# load independent dataset
ind_dataset = pd.read_csv(tst_file, header=None, delimiter=' ')

X_tst = ind_dataset.iloc[:,0:].values

from keras.models import model_from_json
# load json and create model
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model/model.h5")
print("Loaded model from disk")

preds = loaded_model.predict(X_tst) 
print(preds.argmax(axis=-1))

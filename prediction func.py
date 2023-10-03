# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:06:04 2023

@author: sagar
"""

#import streamlit as st
import pickle
import numpy as np
 


# loading the saved model
loaded_model = pickle.load(open("C:/Users/sagar/Desktop/DS Project/trained_model.pkl", 'rb'))


# Sample input data(9th row)
input_data = (0.0,1.0,7.0,1.0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make the prediction
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print('The attack is predicted to be minor.')
else:
    print('The attack is predicted to be major.')

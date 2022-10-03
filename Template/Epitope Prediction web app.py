# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:15:27 2022

@author: Paras Kapoor
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Paras Kapoor/Desktop/Epitope Deployment Streamlit/epitope_model.sav', 'rb'))  # loading the saved model

# Creating a function for prediction

def epitope_prediction(input_data):
    
    
    input_data_as_numpy_array = np.asarray(input_data)   # Conversion of Data into Numpy array

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) # Reshaping the array as we are predicting for one instance
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]) == 0:
        return 'NO epitope is present'
    else:
        return 'Yes epitope is present'
    
    
def main():
    
    # Giving a title to web page
    st.title('Epitope Prediction Web App')
    
    
    # Getting the input data from the user
    F2 = st.text_input('Value of F2')
    F7_6 = st.text_input('Value of F7_6')
    F7_8 = st.text_input('Value of F7_8')
    F8_6 = st.text_input('Value of F8_6')
    F8_9 = st.text_input('Value of F8_9')
    F8_10 = st.text_input('Value of F8_10')
    F9_1 = st.text_input('Value of F9_1')
    F9_6 = st.text_input('Value of F9_6')
    F10_1 = st.text_input('Value of F10_1')
    F10_2 = st.text_input('Value of F10_2')
    F10_4 = st.text_input('Value of F10_4')
    F10_8 = st.text_input('Value of F10_8')
    F10_9 = st.text_input('Value of F10_9')
    F11_3 = st.text_input('Value of F11_3')
    F11_6 = st.text_input('Value of F11_6')
    F11_7 = st.text_input('Value of F11_7')
    F11_8 = st.text_input('Value of F11_8')
    F12_3 = st.text_input('Value of F12_3')
    
    
    # Code for Prediction
    diagnosis= ''   # Null string
    
    # Creating a button for prediction
    
    if st.button("Epitope Test Results"):
        diagnosis = epitope_prediction([F2, F7_6, F7_8, F8_6, F8_9, F8_10, F9_1, F9_6, F10_1, F10_2, F10_4, F10_8, F10_9, F11_3, F11_6, F11_7, F11_8, F12_3])
        
    
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
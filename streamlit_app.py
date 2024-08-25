

import streamlit as st
import pickle
import numpy as np

# Load your model
with open('model2.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict(features):
    # Make prediction with your model
    return model.predict([features])

# Streamlit app
st.title('Model Prediction App')

# User input
st.sidebar.header('User Input')

def get_user_input():
    feature1 = st.sidebar.slider('Glucose', min_value=0, max_value=200, value=0)
    feature2 = st.sidebar.slider('BMI', min_value=0, max_value=100, value=0)
    feature3 = st.sidebar.slider('Age', min_value=0, max_value=100, value=0)
    feature4 = st.sidebar.slider('Pregnancies', min_value=0, max_value=10, value=0)
    return np.array([feature1, feature2, feature3, feature4])

user_input = get_user_input()

# Display user input
st.write('User Input:')
st.write(user_input)

# Prediction
prediction = predict(user_input)
st.write('Prediction:')
st.write(prediction)

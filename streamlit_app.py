

import streamlit as st
import pickle
import numpy as np

# Load your model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict(features):
    # Make prediction with your model
    return model.predict([features])

# Streamlit app
st.title('Model Prediction App')

# User input
st.sidebar.header('User Input')

def get_user_input():
    feature1 = st.sidebar.slider('Feature 1', min_value=0, max_value=100, value=50)
    feature2 = st.sidebar.slider('Feature 2', min_value=0, max_value=100, value=50)
    feature3 = st.sidebar.slider('Feature 3', min_value=0, max_value=100, value=50)
    return np.array([feature1, feature2, feature3])

user_input = get_user_input()

# Display user input
st.write('User Input:')
st.write(user_input)

# Prediction
prediction = predict(user_input)
st.write('Prediction:')
st.write(prediction)

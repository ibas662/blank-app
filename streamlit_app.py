import streamlit as st
import pickle

st.title("🎈 pred")
f1=st.number_input('f1',min_value=1,max_value=10)
f2=st.number_input('f2',min_value=1,max_value=10)
f3=st.number_input('f3',min_value=1,max_value=100)



with open('model.pkl','rb') as file :
  model = pickle.load(file)
var = model.predict([[engine_size, cylinder, fuelconsumption]])
st.write('co2 pred',var[0][0])


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler

st.title('Medical diagnostic App ⚕️')
st.markdown('Does the woman have diabetes or not ?')

# Step1:Load the pickled model
model = open('rfe.pickle' , 'rb')
clf = pickle.load(model)

# Step2:  Get the user input from the front end

pregs = st.number_input('Pregnancies', 0 , 20 , step = 1)
glucose = st.slider('Glucose', 40 , 200 , 40)
bp = st.slider('BloodPressure', 20,140,20)
skin = st.slider('SkinThickness',5,100,5)
insulin = st.slider('Insulin', 14.0 , 846.0 , 14.0)
bmi = st.slider('BMI', 15.0 , 70.0 , 15.0)
dps = st.slider('DiabetesPedigreeFunction', 0.05 , 2.50 , 0.05)
age = st.slider('Age' , 18 , 90 , 21)

# Step3 : Converting user input to model input

data = {
    'Pregnancies' : pregs, 
    'Glucose' : glucose, 
    'BloodPressure' : bp, 
    'SkinThickness' : skin, 
    'Insulin' : insulin,
    'BMI' : bmi, 
    'DiabetesPedigreeFunction' : dps,
    'Age' : age
}

input_data = pd.DataFrame([data])
# st.write(input_data)

# step4 : get the model prediction and print it

prediction = clf.predict(input_data)

if st.button('Prediction'):
    if prediction == 1:
        st.subheader('The woman has diabetes')
    else:
        st.subheader('The woman is healthy')

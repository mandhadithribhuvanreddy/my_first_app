import streamlit as st
import pandas as pd

st.title("Streamlit Demo app")
st.header("Prediction System")
st.subheader("Enter inputs below")

st.write("This app demonstrates ML/DL model deployment")

# Text Input:
name = st.text_input("Enter your Name ")
# Number Input:
number = st.number_input("Enter Age", min_value=1, max_value=100)
# Slider
salary = st.slider("Select Salary ", 10000, 100000)
# Select Box
Gender = st.selectbox("Select Gender", ['Male', 'Female'])
# Radio Button
radio = st.radio("Education Level", ['PhD', 'PG', 'UG'])
# Checkbox
check = st.checkbox("I agree to the terms and conditions")
# File Upload
file = st.file_uploader("Upload Image", type=['jpg','png'])

# Display model output
if st.button("Predict"):
    st.success("Successful Prediction")
if st.button("Clear below chat"):
    st.warning("Click on valid button")

# Display the DataFrame
df = pd.DataFrame({"Age":[23, 45, 67, 53, 98, 17],
                   "Names":["Ajay", "Ram", "Sudarshan", "Abhiram", "Bharath", "Mahesh"],
                   "Salary(K)":[100, 90, 80, 56, 73, 150]})

st.dataframe(df)

# Display the metrics
st.metric("Accuracy", "92%", "+2%")

# Navigation
st.sidebar.title("Navigator")
page = st.sidebar.selectbox("Choose Page", ["Home", "Prediction"])

# Snowfall & Balloons
if st.button("Snow fall"):
    st.snow()

if st.button("Balloon fly"):
    st.balloons()



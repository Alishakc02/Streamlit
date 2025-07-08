import streamlit as st
import pandas as pd

st.title("Chai Sales Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file:", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the uploaded file:")
    st.write(df.head())
else:
    st.warning("Please upload a CSV file.")



if uploaded_file:
    st.subheader('Summary stats')
    st.write(df.describe())
    
    
    
if uploaded_file:
    cities=df['City'].unique()
    selected_city=st.selectbox("Filter by cities", cities)
    filtered_data=df[df['City']==selected_city]
    st.dataframe(filtered_data)

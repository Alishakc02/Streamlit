import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
df=pd.read_csv('final_student_data.csv')

#Now for the dashboard
st.header('Student Record Performance ')
if st.checkbox("Show full dataset"):
    st.dataframe(df)

# Clean names in the DataFrame
df['name'] = df['name'].str.strip().str.lower()

# Clean input
name_input = st.text_input("🔍 Enter student name").strip().lower()

if name_input:
    result = df[df['name'] == name_input]
    
    if not result.empty:
        st.success(f"🎯 Results for: {name_input.title()}")
        st.dataframe(result.T)
    else:
        st.error("No student found with that name.")



st.write("🧾 Column Names in Dataset:")
st.write(df.columns.tolist())

        
        
# Filter by ML Predicted Grade
prediction_filter = st.selectbox("📊 Filter by Predicted Grade", ["All"] + sorted(df["ml_predicted_grade"].unique()))

# Apply filter
filtered_df = df if prediction_filter == "All" else df[df["ml_predicted_grade"] == prediction_filter]

st.subheader("📋 Filtered Students by Predicted Grade")
st.dataframe(filtered_df)

# Filter by subject score (e.g., Math > 60)
score_threshold = st.slider("Minimum Math Score", 0, 100, 50)
filtered_df = filtered_df[filtered_df["math_score"] >= score_threshold]

st.subheader("📋 Filtered Students")
st.dataframe(filtered_df)

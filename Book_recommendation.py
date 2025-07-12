import streamlit as st 
import pandas as pd
import numpy as np

st.title("Book library")

#Upload the file
uploaded_file=st.file_uploader('Upload your csv file:', type=['csv'])

#Function
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the uploaded file:")
    st.write(df.head())
else:
    st.warning("Please upload a CSV file.")

#Datasets
df=pd.read_csv('kindle_data-v2.csv')
df.head(4)
#Fullfill the missing value
df.fillna('', inplace=True)

#Search query
search_query = st.text_input("Search for a book title or author:")

# Filter Data
filtered_df = df[df['title'].str.contains(search_query, case=False) | 
                 df['author'].str.contains(search_query, case=False)]


# Show Results
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.markdown("---")
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(row['imgUrl'], width=120)
        with cols[1]:
            st.subheader(row['title'])
            st.write(f"**Author**: {row['author']}")
            st.write(f"**Rating**: {row['stars']} ⭐")
            st.write(f"**Price**: ${row['price']}")
            if row['isKindleUnlimited']:
                st.markdown(" Available on **Kindle Unlimited**")
            st.markdown(f"[ View on Amazon]({row['productURL']})")
else:
    st.warning("No matching books found.")

import streamlit as st 
import pandas as pd

# Load datasets
df = pd.read_csv('20191226-items.csv')
reviews_df = pd.read_csv('20191226-reviews.csv')  # Make sure this exists

# Search query
search_query = st.text_input("🔍 Search for a product title or brand:")

# Filter data
filtered_df = df[df['title'].str.contains(search_query, case=False, na=False) | 
                 df['brand'].str.contains(search_query, case=False, na=False)]

# Display in pairs (2 per row)
if not filtered_df.empty:
    for i in range(0, len(filtered_df), 2):
        st.markdown("## 🔹 Product Pair")
        st.markdown("---")
        
        row_data = filtered_df.iloc[i:i+2]
        cols = st.columns([1, 0.1, 1])  # Adds spacing between products

        for idx, (col, (_, product)) in enumerate(zip([cols[0], cols[2]], row_data.iterrows())):
            with col:
                

                st.image(product['image'], width=140)
                st.subheader(product['title'])
                st.write(f"**Brand**: {product['brand']}")
                st.write(f"**Rating**: {product['rating']}  ⭐")
                st.write(f"**Price**: ${product['price']}")
                st.markdown(f"[ View on Amazon]({product['url']})")
              




                # Display top 3 reviews for this product
                st.markdown("**Top Reviews:**")
                product_reviews = reviews_df[reviews_df['asin'] == product['asin']].head(3)
                st.write(product_reviews)
                



               

else:
    st.warning("No matching products found.")

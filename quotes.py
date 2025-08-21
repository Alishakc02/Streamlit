import requests
from bs4 import BeautifulSoup
import streamlit as st

st.title(" Quote Finder by Author")
st.write("Enter an author's name to find their quotes from quotes.toscrape.com")

author_input = st.text_input("Author Name (e.g. albert)").lower()

if author_input:
    all_quotes = []
    base_url = "http://quotes.toscrape.com"
    page_url = "/page/1"

    while page_url:
        res = requests.get(base_url + page_url)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            text = quote.find(class_="text").get_text(strip=True)
            author = quote.find(class_="author").get_text(strip=True)
            if author_input in author.lower():
                all_quotes.append((text, author))

        next_btn = soup.find(class_="next")
        page_url = next_btn.a['href'] if next_btn else None

    if all_quotes:
        st.subheader(" Matching Quotes:")
        for quote, author in all_quotes:
            st.markdown(f" {quote} \n\n— {author}")
    else:
        st.warning("No quotes found for that author.")

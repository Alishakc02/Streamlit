import streamlit as st 
import pandas as pd
import yfinance as yf

st.write("""
         #Simple stock price app
         Shown are the stock closing price and volume of Google!!""")

tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)

tickerOf = tickerData.history(start="2010-05-10", end="2020-05-25")

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)
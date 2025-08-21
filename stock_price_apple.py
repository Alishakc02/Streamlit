import streamlit as st 
import pandas as pd
import yfinance as yf

tickerSymbol='AAPL'
tickerData= yf.Ticker(tickerSymbol)
tickerOf= tickerData.history(period='5d')


st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)
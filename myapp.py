import yfinance as yf
import streamlit as st
import pandas as pd
import datetime
d=datetime.date.today()
start_current_month=datetime.date(d.year,d.month,1)

if d.month==12:
    new_year=d.year+1
    new_month=1
else:
    new_year=d.year
    new_month=d.month+1

start_next_month=datetime.date(new_year,new_month,1)

str_start_current_month=start_current_month.isoformat()
str_start_next_month=start_next_month.isoformat()

str_start_current_month=start_current_month.isoformat()
str_start_next_month=start_next_month.isoformat()


st.write("# Stock Price Trend App")
st.write("""## Enter Stock Ticker Symbol
(ex. AAPL, GOOGL, ES=F)""")


tickerSymbol = st.text_input(" ",'GOOGL')
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=d)


st.write("Closing Price")
st.line_chart(tickerDf.Close)
st.write("Stock Volume")
st.line_chart(tickerDf.Volume)

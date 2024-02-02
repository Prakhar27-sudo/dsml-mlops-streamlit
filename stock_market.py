import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
import datetime
import streamlit as st



st.title('Stock Market App')
st.write("This is my chance of getting hike")


ticker_symbol =  st.text_input("Enter the stock ticker symbol:")
start_date = st.date_input("Enter the start date", value=pd.to_datetime("2019-7-6"))
end_date =  st.date_input("Enter the end date", value = pd.to_datetime("today"))



ticker_data = yf.Ticker(ticker_symbol)


hist = ticker_data.history(start = '2022-05-31',end='2023-12-31')
st.write('This is the Ticker Data !!!')
st.write(hist.head())

## we can also use st.dataframe(hist) if the dataset size is too huge

# ### Creating line charts
# st.write("This plot is for Volume of the Stock")
# st.line_chart(hist.Volume)

# st.write("This plot is for Volume of the Price")
# st.line_chart(hist.Close)

col1 , col2 = st.columns(2)

with col1:
    st.write("This plot is for the volume of the stock")
    st.line_chart(hist.Volume)

with col2:
    st.write("This plot is for Volume of the Price")
    st.line_chart(hist.Close)



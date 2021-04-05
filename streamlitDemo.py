# import packages needed
from datetime import date, datetime, time
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# print title
st.title("CIDM6351 Streamlit Demo")
# print plain text
st.write("**Streamlit**: The fastest way to build and share data apps in Python")
# print text formatted by HTML
st.markdown("<h1 style='text-align:center; color:red;'> Sample Stock Price App. </h1>", unsafe_allow_html=True)

st.write('We will use the code learned from previous lecture to build an online application for tracing stock price')

# a list of stock names
stock_names = ['MSFT','AAPL','AMZN','GOOGL']
# select a stock to check
target_stock = st.selectbox('Select a stock to check', options=stock_names)

# get the basic information about the stock
st.markdown('**Stock Information**')
stock = yf.Ticker(target_stock)
stock_info = stock.info
stock_longName = stock_info['longName']
stock_website = stock_info['website']
address = stock_info['address1']
city = stock_info['city']
state = stock_info['state']
country = stock_info['country']
phone = stock_info['phone']
zip = stock_info['zip']

st.write("**Company:**",stock_longName)
st.write("**Address:**",address)
st.write("**City:**",city)
st.write("**State:**",state)
st.write("**Zip:**",zip)
st.write("**Country:**",country)
st.write("**Phone:**",phone)
st.write("**Website:**",stock_website)

st.markdown('**Stock Price**')

# start date of the stock infomation, default is the first day of year 2021
start_date = st.date_input('Start Date', datetime(2021,1,1))
# end date of the stock infomation, default is date of today
end_date = st.date_input("End Date")

# download the stock data based on stock name, start/end date
data = yf.download(target_stock, start_date,end_date)
fig = px.line(
    data, 
    x = data.index, 
    y = ['Open','High','Low','Close'], 
    title = stock_longName+" Stock Price",
    labels = {"value":"Stock Price ($)", "variable":"Price Type"}
    )
st.write(fig)
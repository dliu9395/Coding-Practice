import requests 
import json 
import streamlit as st 


#Getting the data 
pltr_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=PLTR&apikey=JCVIFL6CJKOZX0UV'
pltr_response = requests.get(pltr_url) 
pltr_data = pltr_response.json() 

IVV_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IVV&apikey=JCVIFL6CJKOZX0UV'
IVV_response = requests.get(IVV_url) 
IVV_data = IVV_response.json() 

#Getting the most recent date and closing price 
pltr_time_series_data = pltr_data['Time Series (Daily)']
date = list(pltr_time_series_data.keys())[0]
pltr_closing_price = float(pltr_time_series_data[date]['4. close'])

IVV_time_series_data = IVV_data['Time Series (Daily)']
IVV_closing_price = float(IVV_time_series_data[date]['4. close'])

#Daily percentage Change in price 
pltr_second_last_date = list(pltr_time_series_data.keys())[1]
pltr_second_last_day_closing_price = float(pltr_time_series_data[pltr_second_last_date]['4. close'])
pltr_percentage_change = (pltr_closing_price/pltr_second_last_day_closing_price) - 1 
pltr_percentage_change = "{:.2%}".format(pltr_percentage_change)

IVV_second_last_date = list(IVV_time_series_data.keys())[1]
IVV_second_last_day_closing_price = float(IVV_time_series_data[IVV_second_last_date]['4. close'])
IVV_percentage_change = (IVV_closing_price/IVV_second_last_day_closing_price) - 1 
IVV_percentage_change = "{:.2%}".format(IVV_percentage_change)

st.title("Comparing PLTR Daily Closing Price") 
st.header("Date: {}".format(date))
col1, col2 = st.columns(2)
col1.metric(label = 'PLTR Closing Price', value = "${}".format(pltr_closing_price), delta = "{} daily change".format(pltr_percentage_change))
col2.metric(label = 'S&P500 Index ETF Closing Price', value = "${}".format(IVV_closing_price), delta = "{} daily change".format(IVV_percentage_change))


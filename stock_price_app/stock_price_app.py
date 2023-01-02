import requests 
import json 
import streamlit as st 


#Getting the data 
pltr_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=PLTR&apikey=JCVIFL6CJKOZX0UV'
IVV_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IVV&apikey=JCVIFL6CJKOZX0UV'

def get_data(url): 
    response = requests.get(url) 
    return response.json()

pltr_data = get_data(pltr_url) 
IVV_data = get_data(IVV_url) 

#Getting the most recent date and closing price 
def time_series_data(data): 
    return data['Time Series (Daily)']

pltr_time_series_data = time_series_data(pltr_data) 
IVV_time_series_data = time_series_data(IVV_data)
current_date = list(pltr_time_series_data.keys())[0]

def current_closing_price(data): 
    return float(data[current_date]['4. close']) 

pltr_closing_price = current_closing_price(pltr_time_series_data)
IVV_closing_price = current_closing_price(IVV_time_series_data)

#Daily percentage Change in price 
def percentage_change(data, closing_price): 
    second_last_date = list(data.keys())[1] 
    second_last_day_closing = float(data[second_last_date]['4. close'])
    percentage_change = (closing_price/second_last_day_closing) - 1 
    return "{:.2%}".format(percentage_change)

pltr_percentage_change = percentage_change(pltr_time_series_data, pltr_closing_price)
IVV_percentage_change = percentage_change(IVV_time_series_data, IVV_closing_price)

st.title("Comparing PLTR Daily Closing Price") 
st.header("Date: {}".format(current_date))
col1, col2 = st.columns(2)
col1.metric(label = 'PLTR Closing Price', value = "${}".format(pltr_closing_price), delta = "{} daily change".format(pltr_percentage_change))
col2.metric(label = 'S&P500 Index ETF Closing Price', value = "${}".format(IVV_closing_price), delta = "{} daily change".format(IVV_percentage_change))


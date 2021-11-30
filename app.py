import streamlit as st

import datetime

import requests
'''
# Is Art an unique human expression?

This front queries NVIDIA software 2020'''

italy = st.date_input('Italy')
russia = st.time_input('Russia')
#pickup_datetime = f'{pickup_date} {pickup_time}'
spain = st.number_input('Spain')
#pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
#dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
#dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
#passenger_count = st.number_input('passenger_count',
#                                  min_value=1,
#                                  max_value=8,
#                                  step=1,
#                                  value=1)

# enter here the address of your flask api
url = 'https://taxifare.lewagon.ai/predict'

#params = dict(pickup_datetime=pickup_datetime,
#              pickup_longitude=pickup_longitude,
 #             pickup_latitude=pickup_latitude,
  #            dropoff_longitude=dropoff_longitude,
   #           dropoff_latitude=dropoff_latitude,
    #          passenger_count=passenger_count)

#response = requests.get(url, params=params)

#prediction = response.json()

#pred = prediction['prediction']

#pred

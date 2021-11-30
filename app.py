import streamlit as st

import datetime

import requests
'''
# Is Art a unique human expression?

This front queries NVIDIA software 2020'''

if st.button('Italy'):
    st.write('Italian Art')
elif st.button('Russia'):
    st.write('Russian Art')
elif st.button('Spain'):
    st.write('Spanish Art')


#italy = st.number_input('Italy')

#russia = st.number_input('Russia')
#pickup_datetime = f'{pickup_date} {pickup_time}'
#spain = st.number_input('Spain')
#pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
#dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
#dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
#passenger_count = st.number_input('passenger_count',
#                                  min_value=1,
#                                  max_value=8,
#                                  step=1,
#                                  value=1)
'''
# Would you like to see the noise clip?
'''
if st.button('Italy'):
    st.write('Italian Art')
elif st.button('Russia'):
    st.write('Russian Art')
elif st.button('Spain'):
    st.write('Spanish Art')




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

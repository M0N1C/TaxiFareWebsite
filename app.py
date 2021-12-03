import streamlit as st


import requests

'''
# Is Art a unique human expression?

This front queries NVIDIA software 2020'''

st.write('Select Country')

option_1 = st.checkbox('Italy')
option_2 = st.checkbox('Russia')
option_3 = st.checkbox('Spain')

if option_1 or option_2 or option_3:
    pkl = st.number_input('Choose Pickle and Latent Walk', value=41)
    left, med1, med2, right = st.columns(4)
    with left:
        line = st.button('Line')
    with med1:
        noise = st.button('Noise')
    with med2:
        circular = st.button('Circular')
    with right:
        sphere = st.button('Sphere')

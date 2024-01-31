import streamlit as st

number = st.number_input('Insert a numbers')
st.write('The current number is ', number)

number_1 = st.number_input('Insert second number')
st.write('The current number is ', number_1)

shumzimi = number * number_1
st.write("Vlera e shumezuar", shumzimi)


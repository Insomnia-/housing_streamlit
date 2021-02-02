import streamlit as st
import numpy as np
import pandas as pd

st.title('Housing Prediction')

housing = pd.read_csv('housing.csv')
st.subheader("Housing data in California in 1990s:")
st.dataframe(housing)
st.subheader("Some basic statistics for this dataset:")
st.write(housing.describe())



st.subheader('Map of all houses in California')
st.map(housing)


st.subheader('Map of part of houses in California according to location you choose:')
option = st.selectbox(
    'Which location do you like to investigate?',
     housing['ocean_proximity'].unique())

'You selected: ', option

st.map(housing[housing['ocean_proximity'] == option])


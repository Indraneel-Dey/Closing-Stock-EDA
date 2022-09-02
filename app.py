import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('Closing Stock.csv')
profile = ProfileReport(df)

st.write('Indraneel Dey')
st.write('21f3002696')
st.write('Indian Institute of Technology, Madras')
st.title('Profile Report of Closing Stock of Products')
st.write(df)
st_profile_report(profile)

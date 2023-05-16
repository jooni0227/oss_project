import streamlit as st
import matplotlib as plt
import numpy as np

x=st.slider('Select a Value')
st.write(x,'squared is',x*x)

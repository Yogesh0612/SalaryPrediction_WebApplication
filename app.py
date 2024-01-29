import streamlit as st
from Predict import show_predict_page
from Explore import show_explore_page

choice = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

if choice == "Explore":
    show_explore_page()
else:
    show_predict_page()


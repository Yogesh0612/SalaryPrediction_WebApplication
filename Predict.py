import streamlit as st
import pickle
import numpy as np


def show_predict_page():
    def load_model():
        with open('saved_steps.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    data = load_model()
    regressor = data['model']
    le_country = data['le_country']
    le_education = data['le_education']

    st.title("Software Developer Salary Prediction")

    st.write("""We need some information to predict salary""")

    countries = ['United States of America',
           'United Kingdom of Great Britain and Northern Ireland',
           'Australia', 'Netherlands', 'Germany', 'Sweden', 'France', 'Spain',
           'Brazil', 'Italy', 'Canada', 'Switzerland', 'India', 'Norway',
           'Denmark', 'Israel', 'Poland']

    education = ['Bachelor’s degree', 'No degree', 'Master’s degree', 'Post grad']

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    experience = st.slider("Years of Experience", 0,50,3)

    ok = st.button("Calculate Salary")

    if ok:
        x = np.array([[country, education, experience]])
        x[:,0] = le_country.transform(x[:,0])
        x[:,1] = le_education.transform(x[:,1])
        x = x.astype(float)
        salary = regressor.predict(x)
        st.subheader(f"""The estimated salary is $ {round(salary[0],3)}""")



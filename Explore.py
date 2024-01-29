import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import cleaned_df

def load_data():
    return cleaned_df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write("Stack Overflow Developer Survey 2023")

    def shorten_countries(categories, cutoff):
        categorical_map = {}
        for i in range(len(categories)):
            if categories.values[i] >= cutoff:
                categorical_map[categories.index[i]] = categories.index[i]
            else:
                categorical_map[categories.index[i]] = 'Other'
        return categorical_map

    country_map = shorten_countries(df.Country.value_counts(), 1000)
    df['Country'] = df['Country'].map(country_map)

    data = df['Country'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels = data.index, autopct = '%1.2f%%')
    ax1.axis('equal')
    st.write("## No. of Software Developers by Country ##")
    st.pyplot(fig1)

    st.write("## Mean Salary Based on Country ##")
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending = True)
    st.bar_chart(data)

    st.write("## Mean Salary Based on Experience ##")
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending = True)
    st.line_chart(data)















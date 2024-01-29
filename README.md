# Salary Prediction and Data Exploration
## Overview
This project focuses on predicting software engineer salaries using data collected from the Stack Overflow Developer Survey. The process involves web scraping to obtain the dataset link, downloading the data, cleaning, and transforming it for analysis. A Gradient Boosting Regressor model is trained to predict salaries based on various features.

Key Steps
1. Data Collection
Web scraped Stack Overflow to obtain the dataset link.
Downloaded a zip file containing the survey data.
Extracted the CSV file from the zip archive.
2. Data Cleaning and Transformation
Cleaned the dataset by handling missing values and removing unnecessary columns.
Transformed categorical features using LabelEncoder from scikit-learn.
3. Model Training
Utilized a Gradient Boosting Regressor to predict software engineer salaries.
Employed cross-validation for model evaluation.
4. Deployment with Streamlit
Created a Streamlit web application for user interaction.
Implemented two main features:
Salary Prediction: Allows users to input parameters and predicts the expected salary.
Data Exploration: Provides descriptive statistics and visualizations for better insights into the dataset.
Project Structure
Data Collection: Code for web scraping and dataset retrieval.
Data Cleaning: Jupyter notebook or script for cleaning and transforming the data.
Model Training: Jupyter notebook or script containing the model training process.
Streamlit App: The Streamlit web application code.
Usage
Clone the repository.
Navigate to the project directory.
Run the Streamlit app using streamlit run app.py.
Interact with the app to predict salaries and explore the dataset.
Dependencies
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
BeautifulSoup (for web scraping)

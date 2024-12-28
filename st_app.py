# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1knzGZB2daXq1zpj7aPW2oCmyvgD4Fv8X
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Configurasi Streamlit
st.set_page_config(page_title="Data Science Salaries", layout="wide")

# Title
st.title("📊 Data Science Salaries Dashboard")

# Load Dataset
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    # Load dataset
    dataset = pd.read_csv(uploaded_file)

    # Dataset Overview
    st.subheader("📋 Dataset Overview")
    st.write("First few rows:")
    st.write(dataset.head())

    # General Info
    st.subheader("📃 Dataset Information")
    buffer = []
    dataset.info(buf=buffer)
    info_str = "\n".join(buffer)
    st.text(info_str)

    # Descriptive Statistics
    st.subheader("📊 Descriptive Statistics")
    st.write(dataset.describe(include='all'))

    # Preprocessing
    df_encoded = dataset.copy()
    le = LabelEncoder()

    for column in df_encoded.columns:
        if df_encoded[column].dtype == object:
            df_encoded[column] = le.fit_transform(df_encoded[column])

    # Correlation Heatmap
    st.subheader("📈 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Distribution of Experience Level
    if 'experience_level' in dataset.columns:
        st.subheader("📊 Experience Level Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x='experience_level', data=dataset, palette='Set2', ax=ax)
        ax.set_title("Distribution of Experience Level")
        st.pyplot(fig)

    # Salary Statistics and Histogram
    if 'salary_in_usd' in dataset.columns:
        st.subheader("📈 Salary Statistics and Histogram")
        st.write("Salary Statistics:")
        st.write(dataset['salary_in_usd'].describe())

        fig, ax = plt.subplots()
        sns.histplot(dataset['salary_in_usd'], bins=20, kde=True, color='blue', ax=ax)
        ax.set_title("Salary Distribution (USD)")
        st.pyplot(fig)

    # Remote Ratio Distribution
    if 'remote_ratio' in dataset.columns:
        st.subheader("🏠 Remote Ratio Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x='remote_ratio', data=dataset, palette='muted', ax=ax)
        ax.set_title("Remote Ratio Distribution")
        st.pyplot(fig)

else:
    st.info("👈 Please upload a CSV file to proceed.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import seaborn as sns

# Load some data
iris = sns.load_dataset('iris')

# Add title and header
st.title("Introduction to Streamlit")
st.header("Iris Data Exploration")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.header("This is my dataset:")
    st.dataframe(data=iris)
    # st.table(data=iris)
    # st.write(data=iris)

# Setting up columns
left_column, middle_column, right_column = st.columns([2, 2, 1])

# Widgets: selectbox
species = ["All"]+sorted(pd.unique(iris['species']))
species = left_column.selectbox("Choose a species", species)

# Widgets: radio buttons
show_means = middle_column.radio(
    label='Show Class Means', options=['Yes', 'No'])

import streamlit as st
import pandas as pd
st.title("Data-app")

file = st.file_uploader('Upload your csv file: ',type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data-Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary-Status")
    st.write(df.describe())

if file:
    State = df['State'].unique()
    selected_State = st.selectbox('Filter by States',State)
    filter_data = df[df['State'] == selected_State]
    st.dataframe(filter_data)

import streamlit as st
import pandas as pd

st.title("Depression Detection using ECG ")
st.write("Project by Sonali - 49")
st.success("S3 Bucket Connected ")

file = st.file_uploader("Upload CSV", type="csv")
if file:
    df = pd.read_csv(file)
    st.write(df.head())
    st.button("Predict Depression")
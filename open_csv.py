import streamlit as st
import os
import pandas as pd

#assuming all the csv files are stored in the 'csvs' folder
csv_list = os.listdir("csvs")

st.title("CSV Scanner")

file = st.selectbox("Select a file from the dropdown", options = csv_list)

csv_df = pd.read_csv(open("csvs/"+file))
cols = list(csv_df.columns)

fields = st.multiselect('Select required fields from the file', options = cols)

submit = st.button("Submit")

if submit:
    st.write("  \n")
    st.write("Selected file and fields:")
    st.dataframe(csv_df[fields])

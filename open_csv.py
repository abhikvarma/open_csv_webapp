import streamlit as st
import os
import pandas as pd

#assuming all the csv files are stored in the 'csvs' folder
dir = "csvs"
csv_list = os.listdir(dir)

st.title("CSV Scanner")

#the selected file name is returned 
file = st.selectbox("Select a file from the dropdown", options = csv_list)

#the csv file is read as a pandas dataframe and
#a list of column names are stored
csv_df = pd.read_csv(open("csvs/"+file))
cols = list(csv_df.columns)

#the delected field are stored in a list
fields = st.multiselect('Select required fields from the file', options = cols)

submit = st.button("Submit")

#displays the selected fields from the file
if submit:
    st.write("  \n")
    st.write("Selected file and fields:")
    st.dataframe(csv_df[fields])

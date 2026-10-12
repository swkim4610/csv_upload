import streamlit as st
import pandas as pd

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    df = pd.read_csv(spectra)
    df = df[::-1]
    df['time'] = df.index
    st.write(df)
    st.line_chart(df, x="time", y="Close")

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st
 

gr= pd.read_csv('Banco.csv')
st.title("Datos")
 
 
tab1, tab2 = st.tabs(['macro', 'regalias'])
 
with tab1:
    fig, ax = plt.subplots(1, 4, figsize=(10, 4))
    
    ax[0].plot(gr['TPM1'].dropna())
    
    ax[1].plot(gr['PIB3'].dropna())
    
    ax[2].plot(gr['INF1'].dropna())

    ax[3].plot(gr['DES1'].dropna())

st.pyplot(fig)
 

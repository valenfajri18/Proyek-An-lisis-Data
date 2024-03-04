import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with st.sidebar:
    st.header('Profile')
    
st.title("Air Quality of Dongsi")

st.write("Air Quality of Dongsi is a careful system for assessing, monitoring and analyzing air quality in Dongsi, an area located in Dongcheng District, Beijing, China. In the midst of the complexity of the urban environment, where industrial activity, transportation and dense population can have a significant impact on air quality, this system becomes very important. By paying attention to various parameters such as PM2.5, PM10, SO2, NO2, CO, and O3, Air Quality of Dongsi is able to provide a detailed picture of air conditions. Through available graphs, tables and reports, users can track patterns that emerge from air quality data. They can identify long-term trends, as well as understand seasonal or situational changes in air quality that may occur.")

st.write("Apart from that, Air Quality of Dongsi also provides very useful information for decision making. The data provided by this system can be used to evaluate the effectiveness of pollution control measures that have been implemented and compare the air quality between Dongsi and other regions. Thus, Air Quality of Dongsi is not only an important tool in raising awareness of air pollution problems, but is also a valuable source of information for environmental management and public health efforts in dense urban environments such as Dongsi, Beijing.")

st.title('Information')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

def load_data():
    df = pd.read_csv('Data_Dongsi.csv')
    return df

df = load_data()    
    
with tab1:
    st.header("Level Of Air Pollution In The Dongsi Area")
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    
    pollutant_counts = df[pollutants].mode().iloc[0]

    pollutant_counts_with_pollutants = pd.DataFrame({'Pollutant': pollutants, 'Frequency': pollutant_counts.values})

    pollutant_counts_sorted = pollutant_counts_with_pollutants.sort_values(by='Frequency', ascending=True)

    st.bar_chart(pollutant_counts_sorted.set_index('Pollutant')) 

with tab2:
    st.header("Annual Variations Air Quality in Dongsi")

    Annual_Information = df.groupby('year').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})

    plt.figure(figsize=(8, 4))
    for feature in Annual_Information.columns:
        plt.plot(Annual_Information.index, Annual_Information[feature], label=feature)

    plt.xlabel('Year')
    plt.ylabel('Average Value')
    plt.legend()

    st.pyplot(plt)
    
with tab3:
    st.header("Pollutant Levels Over Time in Dongsi")
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
  
    plt.figure(figsize=(12, 5))
    for pollutant in pollutants:
        plt.plot(df.index, df[pollutant], label=pollutant)

    plt.xlabel('Index', size=15)
    plt.ylabel('Pollutant Level', size=15)
    plt.legend()
    plt.grid(True)
    
    st.pyplot(plt)
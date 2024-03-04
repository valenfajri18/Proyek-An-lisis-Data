import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

with st.sidebar:
    st.header('Description')

st.title("Air Quality Dashboard")

image = Image.open("AirQuality.jpg")

st.image(image, caption='Air Quality Image', width=500, use_column_width=False)

st.write("This platform is designed to provide easy and fast access to the latest data regarding air quality in various regions. By using interactive visualization features, this dashboard allows users to directly monitor air pollution levels in a number of locations, as well as track trends and changes over time. With the Air Quality Dashboard, users can access relevant information about air quality parameters. This data not only provides a better understanding of the current air conditions in an area, but also helps users understand the impact of environmental changes and human activities on air quality.Apart from that, the Air Quality Dashboard also allows users to compare air quality between locations, both within one city and in various cities or regions. In this way, users can gain more comprehensive insight into differences in air quality in various environments. As a widely accessible tool, the Air Quality Dashboard aims to increase awareness of the importance of clean air for the health and well-being of humans and the environment. With information that is easy to understand and access, it is hoped that users can make better decisions in protecting the health of themselves and the surrounding environment, as well as contributing to overall environmental protection efforts.")

def calculate_rfm(data):
    # Hitung RFM Analysis
    if 'Location' in data.columns:
        rfm_data = data.groupby('Location').agg({
            'Date': lambda date: (pd.Timestamp.now().normalize() - pd.to_datetime(date).max()).days,
            'PM2.5': 'mean',
            'ID': 'count'
        }).reset_index()
        rfm_data.columns = ['Location', 'Recency', 'Monetary', 'Frequency']
        return rfm_data
    else:
        st.error("Column 'Location' not found in the uploaded data.")
        return None

def main():
    st.title('RFM Analysis for Air Quality')

    # Upload file CSV dengan data kualitas udara
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        st.subheader('Data Sample')
        st.write(data.head())

        # Hitung RFM Analysis
        rfm_data = calculate_rfm(data)

        if rfm_data is not None:
            st.subheader('RFM Analysis Results')
            st.write(rfm_data)

            # Visualisasi
            st.subheader('RFM Analysis Visualization')

            # Plot Recency
            plt.bar(rfm_data['Location'], rfm_data['Recency'])
            plt.xlabel('Location')
            plt.ylabel('Recency (Days)')
            plt.title('Recency of Air Quality Measurements')
            st.pyplot()

            # Plot Frequency
            plt.bar(rfm_data['Location'], rfm_data['Frequency'])
            plt.xlabel('Location')
            plt.ylabel('Frequency')
            plt.title('Frequency of Air Quality Measurements')
            st.pyplot()

            # Plot Monetary
            plt.bar(rfm_data['Location'], rfm_data['Monetary'])
            plt.xlabel('Location')
            plt.ylabel('Monetary (PM2.5)')
            plt.title('Monetary of Air Quality Measurements')
            st.pyplot()

if __name__ == '__main__':
    main()

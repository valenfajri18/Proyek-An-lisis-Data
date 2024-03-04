import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

with st.sidebar:
    st.header('Home')

st.title("Dongsi Subdistrict, Beijing")

st.write("Dongsi literally Eastern Four or Eastern Quadrangle, is the name of an intersection and its surrounding area located in Dongcheng District, Beijing, China. This intersection has important historical value and is one of the distinctive symbols of the region.Dongsi is located in Dongcheng District, which is part of the historical and cultural center of Beijing. This intersection is formed by four main roads, namely North Dongsi Road, South Dongsi Road, West Dongsi Road, and Inner Chaoyangmen Road. These streets have very old origins, dating back even to the Yuan Dynasty.")

image = Image.open("Dongsi.jpg")

st.image(image, caption='Dongsi Area', width=450, use_column_width=False)

st.write("The name Dongsi is taken from the presence of four paifang gates or typical Chinese gates that stand at the four corners of the intersection. These gates are called Gate of the Four Signs of the East or Four East in Mandarin. These gates are important markers of Dongsi identity.To the south of the Dongsi intersection is the Dongsi Mosque which has a rich history. This mosque was founded in 1356 and then rebuilt in 1447. The presence of this mosque adds to the unique historical and religious nuances of the Dongsi area. Dongsi not only has historical value, but is also the center of daily life for local residents and visitors. Around this intersection are a variety of shops, restaurants and other places of interest that reflect Beijing's busy and diverse urban life.Overall, Dongsi is not just a crossroads, but also an important part of Beijing's history, culture and people's lives.")


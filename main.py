import streamlit as st
import requests

api_key = "kKMlCR9znrFDsTDphaG754Fb32cSeBgDTpIxlObo"
url = "https://api.nasa.gov/planetary/apod?api_key=kKMlCR9znrFDsTDphaG754Fb32cSeBgDTpIxlObo"

# Get the request data as a dictionary
request = requests.get(url)
content = request.json()

# Extraction of the data
date = content["date"]
image = content["hdurl"]
explanation = content["explanation"]

##### STREAMLIT #####
st.set_page_config(layout="wide")

st.title("ASTRONOMY PICTURE OF THE DAY")
st.header(date)
st.image(image, width=400)
st.write(explanation)
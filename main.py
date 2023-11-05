import langchain_helper as lch
import streamlit as st
import utilities.search as search
import utilities.scrape as scrape
from PIL import Image

st.title("Alfred v1.0")

header_image = Image.open('./resources/img.png')
st.image(header_image, caption='A helpful monster that only thinks about research')
website = st.text_input("Website to Scrape")

if website:
    st.write("Scraping website: ", website)
    site = scrape.scrape_website("Pow", website)
    st.info(site)
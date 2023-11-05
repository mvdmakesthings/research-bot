"""Main Module"""

from PIL import Image
import streamlit as st

# import langchain_helper as lch
# import utilities.search as search
import utilities.scrape as scrape
import utilities.summerize as summerize
st.title("Alfred v1.0")

header_image = Image.open('./resources/img.png')
st.image(header_image, caption='A helpful monster that only thinks about research')
website = st.text_input("Website to Scrape")
prompt = st.text_input("Prompt Query")

if website and prompt:
    st.write("Scraping website: ", website)
    site_content = scrape.scrape_website(prompt, website)
    summary = summerize.summerize(prompt, site_content)
    st.info(summary)
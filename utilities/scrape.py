"""Module providing a function to scrape a website page"""

import os
import json
import requests
from bs4 import BeautifulSoup

browserless_api_key = os.getenv("BROWSERLESS_API_KEY")

def scrape_website(objective: str, url: str):
    """Scrape a website given it's objective and url

    Args:
        objective (str): The LLM query to be run against the content of the page.
        url (str): The URL of the website to scrape

    Returns:
        str: Plain Text of the website.
    """    
    print("Scraping website: ", url)
    
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }
    
    data = {
        "url": url
    }
    
    # Convert Python Object to JSON string
    data_json = json.dumps(data)
    
    #Build the request
    post_url = f"https://chrome.browserless.io/content?token={browserless_api_key}"
    response = requests.post(post_url, headers=headers, data=data_json)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        
        print("Website Content: ", text)
        
        return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")
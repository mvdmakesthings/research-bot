
import os
import json
import requests
from bs4 import BeautifulSoup

browserless_api_key = os.getenv("BROWSERLESS_API_KEY")

def scrape_website(objective: str, url: str):
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
        
        if len(text) > 10000:
            output = summary(objective, text)
            return output
        else:
            return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")
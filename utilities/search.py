"""Module providing a function search query Google"""

import pprint
from enum import Enum
from dotenv import load_dotenv
from langchain.utilities import GoogleSerperAPIWrapper

load_dotenv()

class SearchType(Enum):
    """The type of search category as defined by GoogleSerperAPIWrapper

    Args:
        Enum (str): The search type
    """
    SEARCH = "search"
    IMAGES = "images"
    NEWS = "news"
    PLACES = "places"

def run_search(query: str, search_type: SearchType = SearchType.SEARCH):
    """Runs a Google search query and returns the results in JSON string

    Args:
        query (str): The query to search for
        search_type (str, optional): ["images","news", "places"] The Google Serper API 
        can return different results depending on the search type. Defaults to None.
    """
    search = GoogleSerperAPIWrapper(type=search_type.value)
    results = search.results(query)
    
    pprint.pp(results)

    return results
# Add code here

import requests
from bs4 import BeautifulSoup
import pandas as pd

movieNames = []
movieLinks = []

# Link Formats 
"""

base - 'https://www.themoviedb.org'
per movie - 'https://www.themoviedb.org/movie/{movie_id}'
cast - 'https://www.themoviedb.org/movie/{movie_id}/cast'

"""
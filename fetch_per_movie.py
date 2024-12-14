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



per_movie = 'https://www.themoviedb.org/movie/912649'

cast_movie ="https://www.themoviedb.org/movie/912649/cast"

new_page = requests.get(per_movie)
cast_page = requests.get(cast_movie)

#=print(new_page)

#print(new_page)


new_soup = BeautifulSoup(new_page.content,'html.parser')
cast_soup = BeautifulSoup(cast_page.content,'html.parser')
#print(new_soup)

title=new_soup.find("h2").text.strip()
genres = new_soup.find("span",attrs={"class":'genres'}).text.strip()
time = new_soup.find("span",attrs={"class":'runtime'}).text.strip()
rating =new_soup.find("div",attrs={"class":'user_score_chart'})
top_cast= cast_soup.find("ol",attrs={"class":'people credits'}).text.strip("\n").replace("\n", "").replace("\t", "").replace("  ", " ")
print(title)
print(genres)
print(time)
print(rating["data-percent"])
print(top_cast)




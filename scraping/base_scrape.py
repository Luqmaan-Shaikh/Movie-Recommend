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
# End


def get_movies():
    base_url = 'https://www.themoviedb.org'
    page = 1

    
    
    while True:
        
        if len(movieNames) >= 2000:
            break
        
        url = f'{base_url}/movie/?page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        movie_cards = soup.find_all('div', class_='card style_1')
        if not movie_cards:
            break

        for movie in movie_cards:
            title = movie.find('h2')
            # print(title)
            movieNames.append(title.text)
            link = movie.find('a')
            movieLinks.append(link['href'])

        page += 1

if __name__ == "__main__":
    get_movies()
    print(len(movieNames))
    
    df = pd.DataFrame({'Movie Name': movieNames, 'Link': movieLinks})
    df.to_csv('test-10k.csv', index=False)
    print("Done")
    



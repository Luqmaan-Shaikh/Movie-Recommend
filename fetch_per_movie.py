# Add code here
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

movieNames = []
movieLinks = []

# Link Formats 
"""

base - 'https://www.themoviedb.org'
per movie - 'https://www.themoviedb.org/movie/{movie_id}'
cast - 'https://www.themoviedb.org/movie/{movie_id}/cast'

"""


'''
# extract only links 
'''
'''
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
    
    df = pd.DataFrame({ 'Link': movieLinks})
    df.to_csv('./Movie-Recommend/test.csv', index=False)  # saved in test.csv
    print("Done")
    
'''




# Initialize an empty list to store the CSV data
data = []

# opening csv file
with open('Movie-Recommend/test.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        data.append(row)

print(data)  #to print the list


# getting some problem from here #need help from here
for i in data :
    per_movie = f'https://www.themoviedb.org{i[0]}'

    cast_movie =f"https://www.themoviedb.org{i[0]}/cast"

    new_page = requests.get(per_movie)
    cast_page = requests.get(cast_movie)

    #print(new_page)

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
    #print(rating["data-percent"])
    print(top_cast)

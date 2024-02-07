import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')

all_movies =  soup.find_all(name="h3",class_ = "title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("DAY45/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


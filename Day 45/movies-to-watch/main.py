#!/usr/bin/env python3

# --- IMPORTS ---

import requests
import lxml
from bs4 import BeautifulSoup

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline" \
      ".com/movies/features/best-movies-2/"

# --- METHODOLOGY ---

response = requests.get(URL)
empireonline_web_page = response.text

soup = BeautifulSoup(empireonline_web_page, "lxml")

all_movies = soup.find_all(
    name="h3",
    class_="title",
)

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

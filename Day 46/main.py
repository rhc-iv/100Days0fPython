#!/usr/bin/env python3

# --- IMPORTS ---

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

SPTFY_CLIENT_ID = "1da1e49ef56245c097acff03fe1ec616"
SPTFY_CLIENT_SECRET = "58f99ca27a334f00b9aca6d6bec5fcd0"

# Scraping Billboard 100
date = input(
    "Which year do you want to travel to? Type the date in this format "
    "YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span",
                                 class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

# Spotify Authentication

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/?code=AQDwj1M02"
                     "-TLZ_O1gpgFaSO4OUMpltSwytH3Kw0m8J2kPilLUr3lJQeaMakfkeUxxa6279CCNJCtJAX-UqJ1YqgIgyqQNmM4cRXruwyNauRIBErzsJT7YlS2FaJtM0mWojD4jFtPjAbxwb8j4Or1z3mREUd27EUxDuvIuUSBL4_SumbK8Xgo3M9cBjR8U4g",
        client_id=SPTFY_CLIENT_ID,
        client_secret=SPTFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   public=False)
print(playlist)

# Adding songs found into the new playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

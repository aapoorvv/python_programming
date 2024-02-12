import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv,dotenv_values
load_dotenv()
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
header = {
    'Authorization' : f'Bearer 1POdFZRZbvb...qqillRxMr2z'
}

spotify_endpoint = "https://api.spotify.com/v1/search"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

url = "https://www.billboard.com/charts/hot-100/"+date
response = requests.get(url)
movies_page = response.text
soup = BeautifulSoup(movies_page, 'html.parser')
music_list = soup.select("li #title-of-a-story")
name = [name.getText() for name in music_list]
song_titles = [song.replace("\n", "").replace("\t", "") for song in name]
print(song_titles)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="DAY46/venv/token.txt",
        username="apoorv", 
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

year = date.split("-")[0]
# print(year)
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
songs = []


for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    song_uri = result["tracks"]["items"][0]["uri"]
    songs.append(song_uri)
print(songs)

top_100 = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=top_100["id"], items=songs)
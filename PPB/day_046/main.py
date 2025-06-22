import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers
# https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
billboard_url = BASE_URL + date
response = requests.get(url=billboard_url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
song_tags = soup.select(selector="li ul li h3")
song_names = [song.getText().strip() for song in song_tags]

# artists_tags = soup.select(selector="li ul li h3+span")
# song_artists = [artist.getText().strip() for artist in artists_tags]
# songs = [(song, artist) for song, artist in zip(song_names, song_artists)]
# print(songs)

# Go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard
# OAuth explained: https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth
# Authentication with Spotify: https://developer.spotify.com/documentation/web-api/concepts/authorization
# Python Spotify module - Spotipy: https://pypi.org/project/spotipy/
# Spotipy documentation: https://spotipy.readthedocs.io/en/2.25.1/
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt",
        username="andy489",
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
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

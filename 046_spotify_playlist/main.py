import requests
from bs4 import BeautifulSoup
# https://spotipy.readthedocs.io/en/2.25.0/
import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_CLIENT_ID = ""
YOUR_CLIENT_SECRET = ""

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt")
)

user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
# Sign up: https://www.spotify.com/bg-bg/signup
# Go to dev dashboard: https://developer.spotify.com/dashboard and create an app
# Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.
# https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth
# https://developer.spotify.com/documentation/web-api/concepts/authorization

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

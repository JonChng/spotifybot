from bs4 import BeautifulSoup
import requests
import dotenv
import os
import spotipy
from spotipy.oauth2 import  SpotifyOAuth

dotenv.load_dotenv()
secret = os.environ["SPOTIFY-SECRET"]
id = os.environ["SPOTIFY-ID"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=id, client_secret=secret, redirect_uri="http://localhost:8888/callback", scope="playlist-modify-private")
)


# date = input("What year do you want to travel to? Input date in format of (YYYY-MM-DD): ")
#
# url = f"https://www.billboard.com/charts/hot-100/{date}"
#
# response = requests.get("https://www.billboard.com/charts/hot-100/")
# soup = BeautifulSoup(response.text,'html.parser')
#
#
# responses = soup.find_all("h3", class_='a-no-trucate')
# songs = [i.getText().strip() for i in responses]
# print(songs)




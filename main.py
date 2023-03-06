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
user_id = sp.current_user()["id"]

song_list = []

date = input("What year do you want to travel to? Input date in format of (YYYY-MM-DD): ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')


responses = soup.find_all("h3", class_='a-no-trucate')
songs = [i.getText().strip() for i in responses]
year = date[0:4]
start = str(int(year) - 3)
range = f"{start}-{year}"

print(songs)


for song in songs:
    result = sp.search(q=f"track:{song} year:{range}", type="track")
    try:
        song_list.append(result['tracks']['items'][0]['album']['artists'][0]['id'])
    except IndexError:
        print("Song does not exist. " + song)





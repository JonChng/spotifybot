from bs4 import BeautifulSoup
import requests
import dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv()
secret = os.environ["SPOTIFY-SERCRET"]
id = os.environ["SPOTIFY-ID"]




date = input("What year do you want to travel to? Input date in format of (YYYY-MM-DD): ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get("https://www.billboard.com/charts/hot-100/")
soup = BeautifulSoup(response.text,'html.parser')


responses = soup.find_all("h3", class_='a-no-trucate')
songs = [i.getText().strip() for i in responses]
print(songs)




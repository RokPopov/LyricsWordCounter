# variables
import json
import requests

artist = "Taylor Swift"
song_title = "Delicate"
keywords = {"drink"}
url = "https://api.lyrics.ovh/v1/" + artist + "/" + song_title

# fetch lyrics
response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

# determine how many times the keywords are used in the song
statistics = {}
for keyword in keywords:
    statistics[keyword] = lyrics.count(keyword)

print(statistics)

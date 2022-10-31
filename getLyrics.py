import requests
artist = input('What artist would you like to imitate?')
url = "https://api.musixmatch.com/ws/1.1/artist.search?format=json&q_artist=" + artist + "&apikey=928e7168219f3356f5186e940cbf58fa"


# url = "https://api.musixmatch.com/ws/1.1/artist.get?format=json&artist_id=51614128&apikey=928e7168219f3356f5186e940cbf58fa"

payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
response = response.json()
print(response['message']['body']['artist_list'])
# print(response.body.artist_list.artist[0].artist_id)
# print(response.body.artist_list.artist[0].artist_id)



# 1. Get Artist Name
#     a. Artist.search w name
#         - grab artist_id
#     b. track.search w artist_id, page_size = 20, s_track_rating = desc, format = JSON
#         - Grab track_id's
#     c. track.lyrics.get w track_id
#         - Grab lyrics from lyrics_body

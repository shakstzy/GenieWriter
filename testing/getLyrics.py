import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
APIKEYS = ['99980988201f634058717251a5723ce1', '928e7168219f3356f5186e940cbf58fa']
artist = input('What artist would you like to imitate?')
url = "https://api.musixmatch.com/ws/1.1/artist.search?format=json&q_artist=" + artist + "&apikey=" + APIKEYS[1]
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s = Service('/Users/adithkum/Downloads/GenieWriter/chromedriver')
driver = webdriver.Chrome(service=s, options=options)

payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload).json()

artist_id = response['message']['body']['artist_list'][0]['artist']['artist_id']
#Get Track id
url_2 = "https://api.musixmatch.com/ws/1.1/track.search?format=json&q_artist={0}&s_track_rating=desc&page_size=24&f_artist_id={1}&apikey={2}".format(artist, artist_id, APIKEYS[1])
response = requests.request('GET', url_2).json()
track_search = response['message']['body']['track_list']
def get_track_urls(tracks):
    temp_list = []
    for track in track_search:
        temp_list.append(track['track']['track_share_url'])
    return temp_list

track_urls = get_track_urls(track_search)

# for url in track_urls:
#     driver.get(url)

artistStorage = ""

for link in track_urls:
    driver.get(link)
    driver.refresh()
    lyricsContent = driver.find_elements(By.XPATH, "//span[contains(@class, 'lyrics__content__ok')]")
    for webel in lyricsContent:
        artistStorage += webel.text

artistList = artistStorage.split('\n')
print(artistList)

# print(track_urls)

# lyrics_list = []
# for id in track_ids:
#     url_3 = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?format=json&track_id={0}&apikey={1}'.format(track_ids[0], APIKEYS[1])
#     response = requests.request('GET', url_3).json()
#     lyrics = response['message']['body']['lyrics']['lyrics_body']
#     lyrics_list.append(lyrics)

# print(lyrics_list[0])

#['ALL LYRICS LUCID DREAM', 'ALL LYRICS OF GODS PLAN', ... 'ALL LYRICS OF N']

#{same : [1, 2], tool : [no pain no tool, nigga i'm just a tool], }



#print([x for x in track_search][1]['track']['track_id'])
# print(response.body.artist_list.artist[0].artist_id)
# print(response.body.artist_list.artist[0].artist_id)



# 1. Get Artist Name
#     a. Artist.search w name
#         - grab artist_id
#     b. track.search w artist_id, page_size = 20, s_track_rating = desc, format = JSON
#         - Grab track_id's
#     c. track.lyrics.get w track_id
#         - Grab lyrics from lyrics_body




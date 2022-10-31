import lyricsgenius as lg
genius = lg.Genius("5iAKokbxLM9hHsS7LiHILuot9sYecAVaXKvMOIQuhKhdNXIhgQo8m6URTG-cPSkM")
# artist = genius.search_artist('Andy Shauf')
# artist.save_lyrics()
# print(artist)

# from lyricsgenius import genius
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
for s in artist.songs:
    print(s.lyrics)
# artist.save_lyrics()

# print(artist.songs)

# genius = genius(token)
# genius.search_artist('Andy Shauf')
# artist.save_lyrics()

# artist = genius.search_artist('Drake', per_page="10")
# artist = genius.search_artist('Drake')
# artists = []
# while True:
#     try:
#         artists.append(genius.search_artist('Drake', max_songs=10))
#         break
#     except:
#         pass
# artist.save_lyrics()
# print(artists)
# while page:
#     request = genius.artist_songs(artist._id,
#                                   sort='popularity',
#                                   per_page=50,
#                                   page=page,
#                                   )
#     songs.extend(request['songs'])
#     page = request['next_page']
# least_popular_song = genius.search_song(songs[-1]['title'], artist.name)
# print(least_popular_song.lyrics)

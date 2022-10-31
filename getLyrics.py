



# 1. Get Artist Name
#     a. Artist.search w name
#         - grab artist_id
#     b. track.search w artist_id, page_size = 20, s_track_rating = desc, format = JSON
#         - Grab track_id's
#     c. track.lyrics.get w track_id
#         - Grab lyrics from lyrics_body

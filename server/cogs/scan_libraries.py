import os
from colorama import Fore, Back, Style

library = "./music"


# /music/Gomez/Touch/Track 1.mp3
# 
# library
#
# artist_folder = Gomez
#
# alubm_folder = Touch

# parts = ['grentperez', 'When We Were Younger', '02', 'When We Were Younger.mp3']
#
# Gomez

def scan():
    records = []
    artists = os.listdir(library)
    for artist in artists:
        albums = os.listdir(os.path.join(library, artist))

        for album_folder in albums:
            tracks = os.listdir(os.path.join(library, artist, album_folder))
            for track in tracks:
                parts = track.split(" - ", 4)
                #now i have parts
                track_index = parts[-2]
                track_title = parts[-1].rsplit(".", 1) [0]
                path = os.path.join(library, artist, album_folder, track)
                records.append([artist, album_folder, track_index, track_title, path])
                
    return records


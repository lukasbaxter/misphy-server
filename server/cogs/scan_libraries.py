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

        for album in albums:
            tracks = os.listdir(os.path.join(library, artist, album))
            for track in tracks:
                parts = track.split(" - ", 4)
                #now i have parts
                index = parts[-2]
                title = parts[-1].rsplit(".", 1) [0]
                extension = parts[-1].rsplit(".", 1) [1]
                path = os.path.join(library, artist, album, track)
                records.append([artist, album, index, title, extension, path])
                
    return records


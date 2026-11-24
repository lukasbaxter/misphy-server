import os
from colorama import Fore, Back, Style

library = "./music"

def scan():
    artist_folders = os.walk(library)
    for album_folders in artist_folders:
        return album_folders

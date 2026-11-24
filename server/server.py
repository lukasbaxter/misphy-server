import os
import sqlite3
from colorama import Fore, Back, Style
from time import sleep

#misphy cogs
from cogs.scan_libraries import scan

logprefix_db = Fore.CYAN + "DATABASE:" + Fore.WHITE
logprefix_cogheck = Fore.LIGHTGREEN_EX + "COG:" + Fore.WHITE

db = "misphy.db"
connection = None
try:
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS music (
            track_id TEXT,
            track_title TEXT,
            track_album TEXT,
            track_artists INTEGER,
            track_artist_name STRING,
            track_releasedate INTEGER,
            track_length INTEGER,
            location TEXT
        )
    """)
    connection.commit()
    print(logprefix_db, "Created or opened successfuly.")


except sqlite3.Error as error:
    print(logprefix_db, Fore.RED, error)



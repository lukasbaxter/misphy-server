import os
import sqlite3
import pprint
from colorama import Fore, Back, Style
from time import sleep

#misphy cogs
from cogs.scan_libraries import scan

logprefix_db = Fore.CYAN + "DATABASE:" + Fore.WHITE
logprefix_cogheck = Fore.LIGHTGREEN_EX + "COG:" + Fore.WHITE

db = "misphy.db"
connection = None
connection = sqlite3.connect(db)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS music (
        track_artist TEXT,
        track_album TEXT,
        track_index INTEGER,
        track_title TEXT,
        track_extension TEXT,
        track_path TEXT
    )
""")
connection.commit()
print(logprefix_db, "Created or opened successfuly.")

records = scan()


cursor.executemany(
    """
    INSERT INTO music (track_artist, track_album, track_index, track_title, track_extension, track_path) VALUES (?, ?, ?, ?, ?, ?)
""", records
)
connection.commit()
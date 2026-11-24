import os
import sqlite3
import pprint
import sys
import time
import logging
from fastapi import FastAPI

from colorama import Fore, Back, Style
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#misphy cogs
from cogs.scan_libraries import scan
from cogs.scan_libraries import library

logprefix_db = Fore.CYAN + "DATABASE:" + Fore.WHITE
logprefix_cogheck = Fore.LIGHTGREEN_EX + "COG:" + Fore.WHITE


app = FastAPI()
db = "misphy.db"

connection = None
connection = sqlite3.connect(db, check_same_thread=True)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS music (
        track_artist TEXT,
        track_album TEXT,
        track_index INTEGER,
        track_title TEXT,
        track_extension TEXT,
        track_path TEXT,
        UNIQUE(track_path)
    )
""")
connection.commit()
print(logprefix_db, "Created or opened successfuly.")

def updateDB():
    connection = sqlite3.connect(db, check_same_thread=True)
    cursor = connection.cursor()
    records = scan()

    cursor.executemany(
        """
        INSERT OR IGNORE INTO music (track_artist, track_album, track_index, track_title, track_extension, track_path) VALUES (?, ?, ?, ?, ?, ?)
    """, records
    )

    connection.commit()

# SELECT * FROM music WHERE track_artist LIKE "%<query>%" OR track_title LIKE "%<query>%"


@app.get("/api/v1/search")
async def search(query: str = None):
    cursor.execute("""
        SELECT * FROM music WHERE track_title LIKE ? OR track_artist LIKE ?
    """, ["%" + query + "%"]*2)
    return cursor.fetchall()

updateDB()
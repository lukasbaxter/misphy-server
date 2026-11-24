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
greeting = "hello from server.py"

@app.get("/")
async def fastapiGreeting():
    return greeting

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



class OnMyWatch:
    watchDirectory = library
    def __init__(self):
        self.observer = Observer()

    def run(self):
        handler = Handler()
        self.observer.schedule(handler, self.watchDirectory, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return

        if event.event_type == "created":
            updateDB()
            print(logprefix_db, "Added:", event.src_path)

        elif event.event_type == "deleted":
            updateDB()
            print(logprefix_db, "Removed:", event.src_path)

if __name__ == "__main__":
    updateDB()
    watch = OnMyWatch()
    watch.run()


# SELECT * FROM music WHERE track_artist LIKE "%<query>%" OR track_title LIKE "%<query>%"
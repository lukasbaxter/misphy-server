import sqlite3
import time


db = "misphy.db"
connection = None
connection = sqlite3.connect(db, check_same_thread=True)
cursor = connection.cursor()

while True:
    cursor.execute("SELECT COUNT(1) from music")
    print(cursor.fetchone())
    time.sleep(0.1)
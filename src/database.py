import sqlite3
from sqlite3 import Error


def __init__(self, db_file):
    self.db_file = db_file

def conn(self):
    global conn
    conn = None
    try:
        conn = sqlite3.connect(self)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

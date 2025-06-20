#!/usr/bin/env python3

import sqlite3
import sys

DB = "project.db"

def add_mantra():
    mantra = input(": ").strip()
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO mantras VALUES (NULL, ?)', (mantra,))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        add_mantra()
    else:
        print(":(")

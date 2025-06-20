#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("project.db")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS mantras (id INTEGER PRIMARY KEY, mantra TEXT)')
conn.commit()
conn.close()

#!/usr/bin/env python3

import sqlite3
import sys

DB = 'project.db'

def show_mantras():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        if '--all' in sys.argv[1:]:
            c.execute('SELECT * FROM mantras')
            for row in c.fetchall():
                print(f"{row[0]} -> {row[1]}")
        elif len(sys.argv) == 1:
            c.execute('SELECT * FROM mantras ORDER BY RANDOM() LIMIT 1')
            result = c.fetchone()
            print(f"\n{result[1]}\n")
        else:
            try:
                mantra_id = int(sys.argv[1])
                c.execute('SELECT * FROM mantras WHERE id = ?', (mantra_id,))
                result = c.fetchone()
                if result:
                    print(f" {result[0]} -> {result[1]}")
                else:
                    print("No mantra found with that ID")
            except ValueError:
                print("Invalid ID - must be integer")

if __name__ == "__main__":
    show_mantras()

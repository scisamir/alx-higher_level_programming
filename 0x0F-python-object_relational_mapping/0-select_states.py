#!/usr/bin/python3
"""
Get all states
"""
from sys import argv
import MySQLdb


db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)

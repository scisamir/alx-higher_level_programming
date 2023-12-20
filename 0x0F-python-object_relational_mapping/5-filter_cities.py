#!/usr/bin/python3
"""
Lists all cities of a state from input database
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name = %s \
            ORDER BY cities.id ASC",
                (argv[4],)
                )
    rows = cur.fetchall()

    for i, row in enumerate(rows):
        if (i + 1 == len(rows)):
            print(row[0], end="")
        else:
            print(row[0], end=", ")
    print()

    cur.close()
    db.close()

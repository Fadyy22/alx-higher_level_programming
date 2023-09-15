#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states \
        ON states.id = cities.state_id \
        WHERE states.name=%s",
        (sys.argv[4],),
    )
    cities = cur.fetchall()
    for city in cities:
        for city_name in city:
            if cities.index(city) == len(cities) - 1:
                print(city_name, end="")
            else:
                print(city_name, end=", ")
    print()

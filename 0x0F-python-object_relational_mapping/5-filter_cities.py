#!/usr/bin/python3
"""Module lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = conn.cursor()
    cur.execute("""
    SELECT cities.name FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id;
    """, (argv[4], ))
    results = cur.fetchall()
    if len(argv) == 5:
        city_names = ", ".join(city[0] for city in results)
        print(city_names)
    cur.close()
    conn.close()

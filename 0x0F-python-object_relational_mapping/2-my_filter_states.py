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
    SELECT * FROM states WHERE name = '{}'
    ORDER BY states.id
    """.format(argv[4]))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

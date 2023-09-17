#!/usr/bin/python3
"""
Script that lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)

"""

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=usr, passwd=pwd, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT c.name \
                FROM cities c INNER JOIN states s \
                ON c.state_id = s.id WHERE s.name = %s\
                ORDER BY c.id", (state_name, ))
    rows = cur.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")

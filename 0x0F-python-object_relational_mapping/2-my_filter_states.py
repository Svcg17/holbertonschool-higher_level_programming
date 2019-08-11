#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv
db = MySQLdb.connect(host='localhost', port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()

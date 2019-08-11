#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    v = '''SELECT cities.name FROM states
           INNER JOIN cities ON states.id = cities.state_id
           WHERE states.name=%s ORDER BY cities.id'''
    cur.execute(v, (sys.argv[4],))
    rows = cur.fetchall()
    for i in range(0, len(rows)):
        if i != len(rows) - 1:
            print("{}, ".format(rows[i][0]), end="")
        else:
            print("{}".format(rows[i][0]))
    cur.close()
    db.close()

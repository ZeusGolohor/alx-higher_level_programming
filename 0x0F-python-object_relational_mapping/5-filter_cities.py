#!/usr/bin/python3
"""
This script is used to lists all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb


def run():
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbe = sys.argv[3]
    stt = sys.argv[4]
    conn = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=usr,
                            passwd=pwd,
                            db=dbe,
                            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                LEFT JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC", (stt,))
    query_rows = cur.fetchall()
    i = 0
    leng = len(query_rows)
    while (i < leng):
        print(query_rows[i][0], end='')
        if (leng != (i + 1)):
            print(', ', end='')
        else:
            print()
        i = i + 1
    if (leng == 0):
        print()
    cur.close()
    conn.close()


if __name__ == "__main__":
    run()

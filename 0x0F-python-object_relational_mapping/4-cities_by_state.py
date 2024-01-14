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
    conn = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=usr,
                            passwd=pwd,
                            db=dbe,
                            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                LEFT JOIN states ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    run()

#!/usr/bin/python3
"""
This script is used to lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    sss = sessionmaker(bind=engine)
    session = sss()
    for state in session.query(State).order_by(asc(State.id)):
        print('{}: {}'.format(state.id, state.name))

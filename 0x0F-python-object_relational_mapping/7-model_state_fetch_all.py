#!/usr/bin/python3
"""
This script is used to lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def run():
    """
    This is a method to make sure code dont run unless its needed
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(asc(State.id)):
        print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    run()
    session.close()

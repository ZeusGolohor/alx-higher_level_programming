#!/usr/bin/python3
"""
This script that contains the class definition
of a State and an instance Base = declarative_base():
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
    MetaData
)

mtd = MataData()
Base = declarative_base(metadata=mtd)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(
                           'root',
                           'root',
                           'hbtn_0e_6_usa',
                           pool_pre_ping=True)
                       )

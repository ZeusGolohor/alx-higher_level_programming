#!/usr/bin/python3
"""
This script that contains the class definition
of a State and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

mtd = MetaData()
Base = declarative_base(metadata=mtd)


class City(Base):
    """
    This is a state class also used to manage state db.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))

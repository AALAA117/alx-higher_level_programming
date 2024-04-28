#!/usr/bin/python3
"""
Module contains the class definition of a State inherits from Base
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """contains the class definition of a State"""
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

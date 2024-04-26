#!/usr/bin/python3
"""
Module contains the class definition of a State inherits from Base
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """contains the class definition of a State"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

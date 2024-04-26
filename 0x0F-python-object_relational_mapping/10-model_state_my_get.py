#!/usr/bin/python3
"""
Module contains the class definition of a State inherits from Base
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        q = session.query(State.id).filter(State.name == sys.argv[4]).all()
        print(q[0][0])
    except Exception as err:
        print("Not found")

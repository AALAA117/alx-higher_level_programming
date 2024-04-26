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
    q = session.query(State).first()
    if q is None:
        print("Nothing")
    else:
        print("{}: {}".format(q.id, q.name))

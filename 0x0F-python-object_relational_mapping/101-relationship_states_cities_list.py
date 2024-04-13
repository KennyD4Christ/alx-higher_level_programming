#!/usr/bin/python3
"""
Script to list all State objects and corresponding City objects in the
database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all State objects and corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Displaying results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

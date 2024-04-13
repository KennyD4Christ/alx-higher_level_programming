#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument from
the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database "
              "state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    engine_string = 'mysql+mysqldb://' + '{}:{}@localhost:3306/{}'.format(
        username, password, database)
    engine = create_engine(engine_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

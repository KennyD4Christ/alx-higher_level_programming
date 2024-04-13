#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    engine_string = 'mysql+mysqldb://' + '{}:{}@localhost:3306/{}'.format(
        username, password, database)
    engine = create_engine(engine_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)
        session.commit()

    session.close()

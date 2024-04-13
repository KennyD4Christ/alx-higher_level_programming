#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states(username, password, db_name):
    """
    Delete all State objects with a name containing the letter "a"
    from the database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
    """
    # Create MySQL connection
    engine_string = 'mysql+mysqldb://' + '{}:{}@localhost:3306/{}'.format(
        username, password, db_name)
    engine = create_engine(engine_string)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query for states containing the letter "a" in their name
    states_query = session.query(State).filter(State.name.like('%a%'))
    states_to_delete = states_query.all()

    # Delete the states
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    deleted_states_count = len(states_to_delete)
    message = "Deleted {} state(s) with name containing 'a'"
    print(message.format(deleted_states_count))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    delete_states(username, password, db_name)

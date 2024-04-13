#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, db_name):
    """
    Change the name of a State object in the database.

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

    # Query for the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Change the name to New Mexico
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
        print("State name changed successfully.")
    else:
        print("State with id 2 not found.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

change_state_name(username, password, db_name)

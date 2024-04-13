#!/usr/bin/python3
"""
This script retrieves and prints the first State object from the database
hbtn_0e_6_usa.

It utilizes SQLAlchemy to connect to the database and efficiently
fetches only the first state object, sorted by ID, without retrieving all
states beforehand. It handles the case of an empty table by printing "Nothing".
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State  # Import State from model_state

if __name__ == "__main__":
    # Get username, password, and database name from command-line arguments
    username = input("Username: ")
    password = input("Password: ")
    database = input("Database name: ")

    # Create a connection engine
    engine_string = f'mysql://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(engine_string)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object, sorted by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result (or "Nothing" if no state found)
    if first_state:
        print(first_state)
    else:
        print("Nothing")

    # Close the session
    session.close()

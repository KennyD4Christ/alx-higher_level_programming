#!/usr/bin/python3
"""
This script fetches and lists all State objects from the database hbtn_0e_6_usa

It utilizes SQLAlchemy to connect to the database and retrieve State objects.
The results are sorted by their IDs in ascending order.
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

    # Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(state)

    # Close the session
    session.close()

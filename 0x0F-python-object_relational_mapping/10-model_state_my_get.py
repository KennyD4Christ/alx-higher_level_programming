#!/usr/bin/python3
"""
This script retrieves and prints the State object with the provided name from
the database hbtn_0e_6_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State  # Import State from model_state

if __name__ == "__main__":
    # Get username, password, database name, and state name from
    # command-line arguments
    username = input("Username: ")
    password = input("Password: ")
    database = input("Database name: ")
    state_name = input("State name: ")

    # Create a connection engine
    engine_string = f'mysql://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(engine_string)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Escape the user-provided state name to prevent SQL injection
    safe_state_name = session.escape(state_name).decode()

    # Query the state with the escaped name (using LIKE for flexibility)
    state_query = session.query(State).filter(State.name.like(safe_state_name))
    state = state_query.first()

    # Print the result (or "Not found" if no state found)
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

#!/usr/bin/python3
"""
This script retrieves and lists all State objects containing the letter
'a' from the database hbtn_0e_6_usa.
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

    # Query states containing 'a', sorted by id (using LIKE operator)
    states_with_a_query = session.query(State).filter(State.name.like('%a%'))
    states_with_a = states_with_a_query.order_by(State.id).all()

    # Print the results
    if states_with_a:
        for state in states_with_a:
            print(state)
    else:
        print("No state found")

    # Close the session
    session.close()

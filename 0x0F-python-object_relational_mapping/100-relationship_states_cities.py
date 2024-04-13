#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_city(username, password, db_name):
    """
    Create the State "California" with the City "San Francisco".

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

    # Create California state
    california = State(name='California')

    # Create San Francisco city
    san_francisco = City(name='San Francisco', state=california)

    # Add both objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

    print("State 'California' and city 'San Francisco' created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage_info = "Usage: python 100-relationship_states_cities.py " \
                     "<username> <password> <database>"
        print(usage_info)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    create_state_city(username, password, db_name)

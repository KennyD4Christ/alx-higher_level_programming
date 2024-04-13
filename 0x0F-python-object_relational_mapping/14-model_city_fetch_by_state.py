#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, db_name):
    """
    Fetch and print all City objects from the database hbtn_0e_14_usa.

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

    # Query for all City objects and sort by id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage_info = "Usage: " \
                     "python 14-model_city_fetch_by_state.py " \
                     "<username> <password> <database>"
        print(usage_info)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    fetch_cities_by_state(username, password, db_name)

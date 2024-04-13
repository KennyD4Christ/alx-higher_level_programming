#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating California state
    california = State(name="California")

    # Creating San Francisco city
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)

    session.commit()

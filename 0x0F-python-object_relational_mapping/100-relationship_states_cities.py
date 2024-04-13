#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
in the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Get MySQL username, password, and database name from command-line
    # arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to establish a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password, db_name))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    california = State(name="California")

    # Add the State object to the session
    session.add(california)

    # Commit the transaction
    session.commit()

    # Create a new City object
    san_francisco = City(name="San Francisco", state=california)

    # Add the City object to the session
    session.add(san_francisco)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()

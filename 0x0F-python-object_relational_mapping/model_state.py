#!/usr/bin/python3
"""
This module defines the State class for object-relational mapping (ORM)
representing states in a database
"""


from sqlalchemy import create_engine, Column, Integer, String, declarative_base
Base = declarative_base()


class State(Base):
    """Represents a state in a database.

    This class maps to the `states` table in a MySQL database.
    """

    # Define table columns
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    # (Optional methods for interacting with the database can be added here)

# Example usage (assuming you have a database engine defined elsewhere)


engine = create_engine('mysql://user:password@localhost:3306/database_name')
Base.metadata.create_all(engine)

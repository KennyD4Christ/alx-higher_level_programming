#!/usr/bin/python3
"""
This module contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base


class State(Base):
    """
    Class representing a state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

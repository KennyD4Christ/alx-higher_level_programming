#!/usr/bin/python3
"""
Module 101-add_attribute

Defines a function that adds a new attribute to an object if it's possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
        - obj: The object to which the attribute is to be added.
        - attribute (str): The name of the attribute.
        - value: The value of the attribute.
    Raises:
        - TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)

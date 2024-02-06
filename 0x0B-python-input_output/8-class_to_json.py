#!/usr/bin/python3
"""Module for serializing objects to JSON."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for
    JSON serialization

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Dictionary description with simple data structure for
        JSON serialization.
    """
    return obj.__dict__

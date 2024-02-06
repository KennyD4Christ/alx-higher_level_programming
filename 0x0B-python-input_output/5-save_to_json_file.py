#!/usr/bin/python3
"""Module for saving an object to a text file using a JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to which the object will be saved.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

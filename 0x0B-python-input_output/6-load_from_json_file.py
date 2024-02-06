#!/usr/bin/python3
"""Module for loading an object from a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        obj: The object loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

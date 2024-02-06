#!/usr/bin/python3
"""Module for appending a string to the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to which the string will be
        appended. Defaults to "".
        text (str): The string to be appended to the file. Defaults to "".

        Returns:
            int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        nb_characters_added = f.write(text)
        return nb_characters_added

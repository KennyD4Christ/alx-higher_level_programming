#!/usr/bin/python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
       the number of characters written.

       Args:
        filename (str): The name of the file to be written. Defaults to "".
        text (str): The string to be written to the file. Defaults to "".

        Returns:
            int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters

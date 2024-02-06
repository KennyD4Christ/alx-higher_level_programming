#!/usr/bin/python3
"""Module for reading a text file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    read_file()

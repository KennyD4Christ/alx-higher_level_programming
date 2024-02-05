#!/usr/bin/python3
"""
This is the MyList module.
"""


class MyList(list):
    """
    MyList class inherits from list and provides additional functionality.

    Public Methods:
        print_sorted(self): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))

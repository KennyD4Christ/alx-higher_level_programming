#!/usr/bin/python3
"""
Square class definition.
"""


class Square:
    """
    This is a square class.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            - size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

        # Validate size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

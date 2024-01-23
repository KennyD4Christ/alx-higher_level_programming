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

    @property
    def size(self):
        """
        Getter method to retrieve the current value of the size attribute.

        Returns:
            - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the value of the size attribute.

        Parameters:
            - value (int): The new size value.

        Raises:
            - TypeError: If value is not an integer.
            - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            - int: The area of the square.
        """
        return self.__size ** 2

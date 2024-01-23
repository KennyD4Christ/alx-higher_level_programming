#!/usr/bin/python3
"""
Square class definition.
"""


class Square:
    """
    This is a square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
            - size (int, optional): The size of the square. Default is 0.
            - position (tuple, optional): The position of the square.
            Default is (0, 0).
        """
        self.size = size  # Using the setter to validate size
        self.position = position  # Using the setter to validate position

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

    @property
    def position(self):
        """
        Getter method to retrieve the current value of the
        position attribute.

        Returns:
            - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the value of the position attribute.

        Parameters:
            - value (tuple): The new position value.

        Raises:
            - TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        else:
            self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' and considering
        the position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

#!/usr/bin/python3

"""
Define a class Square.
"""


class Square:
    """
    Square class with size attribute and area method.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            - size (int or float, optional): The size of the square.
            Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            - int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
            - value (int or float): The new size value.

        Raises:
            - TypeError: If value is not a number (float or integer).
            - ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            - int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison for squares based on area.

        Parameters:
            - other (Square): Another square object.

        Returns:
            - bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()


# Example usage:
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

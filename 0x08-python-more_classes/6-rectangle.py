#!/usr/bin/python3
"""
Module for defining a Rectangle class
"""


class Rectangle:
    """
    Rectangle class with private attributes width and height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
            value (int): The value to set as the width.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Parameters:
            value (int): The value to set as the height.
        Raises:
            TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width != 0 and self.__height != 0:
            result = 2 * (self.__width + self.__height)
        else:
            result = 0

        return result

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rows = ['#' * self.__width for _ in range(self.__height)]
            result = "\n".join(rows)
            return result

    def __repr__(self):
        """
        Returns a representation of the Rectangle.
        Returns:
            str: A representation of the Rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

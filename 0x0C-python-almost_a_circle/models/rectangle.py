#!/usr/bin/python3
"""Module defining Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """
        Return dictionary representation of the rectangle.

        Returns:
        dict: Dictionary representation of the rectangle.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return (
            f"[Rectangle] "
            f"({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of the rectangle.

        Args:
            *args: List of arguments - no-keyworded arguments.
            **kwargs: Keyworded arguments, represents attributes and values.
        """
        if args:
            arg_names = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                if key in ['width', 'height', 'x', 'y']:
                    value = int(value)
                setattr(self, key, value)

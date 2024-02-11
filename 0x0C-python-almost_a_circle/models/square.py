#!/usr/bin/python3
"""Module for Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        width (int): Width of the square.
        height (int): Height of the square.
        x (int): x-coordinate of the square.
        y (int): y-coordinate of the square.
        id (int): Identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance.
        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): Identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): Size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the square.

        Args:
            *args: List of arguments - no-keyworded arguments.
            **kwargs: Keyworded arguments, represents attributes and values.
        """
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for arg_name, value in zip(arg_names, args):
                if arg_name == 'size':
                    value = int(value)
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                elif arg_name in ['width', 'height']:
                    value = int(value)
                    setattr(self, arg_name, value)
                else:
                    setattr(self, arg_name, value)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    value = int(value)
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Return dictionary representation of the square.

        Returns:
        dict: Dictionary representation of the square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

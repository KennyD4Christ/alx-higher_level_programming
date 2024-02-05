#!/usr/bin/python3
"""
Module 100-my_int

Defines a MyInt class that inherits from int.
"""


class MyInt(int):
    """
    Represents a rebel integer class with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.
        """
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

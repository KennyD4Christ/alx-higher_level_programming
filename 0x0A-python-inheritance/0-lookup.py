#!/usr/bin/python3
"""
This is a lookup class
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object for which attributes and methods are to be looked up.

    Returns:
        A list containing the names of attributes and methods of the object.
    """

    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        y_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))

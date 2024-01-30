#!/usr/bin/python3
"""
    Defines a locked class.
"""

class LockedClass:
    """
    Defines a locked class.
    A class that prevents the dynamic creation of new instance attributes,
    except 'first_name'.
    """
    __slots__ = ['first_name']

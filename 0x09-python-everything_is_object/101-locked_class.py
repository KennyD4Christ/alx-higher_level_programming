#!/usr/bin/python3
class LockedClass:
    """A class that prevents the dynamic creation of new instance attributes,
    except 'first_name'."""
    __slots__ = ['first_name']

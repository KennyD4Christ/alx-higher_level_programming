#!/usr/bin/python3
class LockedClass:
    """A class that restricts attribute assignment, allowing only 'first_name'.

    Attributes:
        None
    """

    def __setattr__(self, name, value):
        """Control attribute assignment for LockedClass.

        Args:
            name (str): The name of the attribute being assigned.
            value: The value being assigned to the attribute.

        Raises:
            AttributeError: If the attribute being assigned is not 'first_name'.
        """

#!/usr/bin/python3
"""Module defining a Student class."""


class Student:
    """Class defining a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings specifying attribute names to
            retrieve.

        Returns:
            dict: Dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with values
        from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.

        """
        for key, value in json.items():
            setattr(self, key, value)

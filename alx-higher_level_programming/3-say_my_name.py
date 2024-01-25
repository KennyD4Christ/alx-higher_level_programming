#!/usr/bin/python3
"""
Function to print a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the person's name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + (" " + last_name if last_name else "")
    print("My name is {}".format(full_name))


# Example usage
if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)

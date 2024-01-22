#!/usr/bin/python3

def raise_exception():
    raise TypeError("Exception raised")


# Example usage:
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError:
        print("Exception raised")

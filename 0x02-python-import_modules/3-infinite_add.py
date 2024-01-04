#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Skip the first element of argv, which is the script name
    args = argv[1:]

    # Convert arguments to integers and sum them
    result = sum(int(arg) for arg in args)

    # Print the result followed by a new line
    print(result)

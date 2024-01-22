#!/usr/bin/python3

def safe_print_integer(value):
    # Use try-except to handle potential ValueError
    try:
        # Print the integer value followed by a new line
        print("{:d}".format(value))
        # Return True to indicate successful printing
        return True
    except ValueError:
        # Handle ValueError if the value is not convertible to an integer
        return False


# Check if the script is being run directly
if __name__ == "__main__":
    # Example usage:
    result = safe_print_integer(42)
    print("Printing successful:", result)
    result = safe_print_integer("not_an_integer")
    print("Printing successful:", result)

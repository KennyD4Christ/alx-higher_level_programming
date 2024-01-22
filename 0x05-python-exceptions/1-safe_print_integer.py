#!/usr/bin/python3

def safe_print_integer(value):
    # Use try-except to handle potential ValueError
    try:
        # Print the integer value followed by a new line
        print("{:d}".format(value))
        # Return True to indicate successful printing
        return True
    except (ValueError, TypeError):
        # Handle ValueError if the value is not convertible to an integer
        return False


# Check if the script is being run directly
if __name__ == "__main__":
    # Example usage:
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

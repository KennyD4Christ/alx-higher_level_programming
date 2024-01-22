#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a variable to count the elements printed
    elements_printed = 0
    # Use try-except to handle potential IndexError
    try:
        # Iterate through the list up to the specified number of elements (x)
        for i in range(x):
            # Print the element on the same line
            print(my_list[i], end="")
            # Increment the count of elements printed
            elements_printed += 1
        # Print a new line after printing the specified number of elements
        print()
    except IndexError:
        # Handle IndexError if x is greater than the length of my_list
        print()
    # Return the real number of elements printed
    return elements_printed


if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    num_elements_printed = safe_print_list(my_list, 3)
    print(f"Number of elements printed: {num_elements_printed}")

#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use indexing to get the first and second elements of each tuple
    a_first = tuple_a[0] if len(tuple_a) >= 1 else 0
    a_second = tuple_a[1] if len(tuple_a) >= 2 else 0

    b_first = tuple_b[0] if len(tuple_b) >= 1 else 0
    b_second = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Calculate the sum of corresponding elements
    result_first = a_first + b_first
    result_second = a_second + b_second

    # Return the result as a tuple
    return (result_first, result_second)


# Example usage
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))

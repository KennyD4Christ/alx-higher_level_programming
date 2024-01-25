#!/usr/bin/python3
"""
Function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The number to divide the matrix elements.

    Returns:
        list of lists: The new matrix with elements divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
        or if each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(all(isinstance(num, (int, float)) for num in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    result_matrix = matrix_divided(matrix, 3)
    print(result_matrix)
    print(matrix)  # Original matrix remains unchanged

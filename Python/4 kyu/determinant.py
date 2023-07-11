from typing import List


def determinant(matrix: List[List[float]]) -> float:
    """
    Calculates the determinant of a square matrix.

    Args:
        matrix: A square matrix represented as a list of lists.

    Returns:
        The determinant of the matrix.

    Raises:
        ValueError: If the input matrix is not square.
    """
    if not matrix:
        raise ValueError("Empty matrix")

    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Input matrix is not square")

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0.0
    for i in range(n):
        sub_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        sign = (-1) ** i
        cofactor = matrix[0][i]
        det += sign * cofactor * determinant(sub_matrix)

    return det


# -- alternative solution --
# import numpy as np
#
# def determinant(a):
#     return round(np.linalg.det(np.matrix(a)))

if __name__ == "__main__":
    assert determinant([[5]]) == 5
    assert determinant([[4, 6], [3, 8]]) == 14
    assert determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]) == 10
    print("All tests passed successfully!")

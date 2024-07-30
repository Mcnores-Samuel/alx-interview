#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix 90 degrees clockwise in place.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    if not all(len(row) == len(matrix) for row in matrix):
        return

    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom element to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move right element to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top

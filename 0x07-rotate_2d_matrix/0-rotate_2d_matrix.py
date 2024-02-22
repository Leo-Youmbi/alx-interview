#!/usr/bin/python3
"""2D Matrix Rotation module.
"""

def rotate_2d_matrix(matrix):
    """Rotates the 2D matrix given by 90 degrees
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

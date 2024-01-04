#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n: int):
    """Returns the Pascal Triangle

    Args:
        n (int): The length of the triangle

    Returns:
        list: A list of lists
    """
    triangle = []
    if n > 0:
        for i in range(n):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1, 1])
            else:
                prev_array = triangle[-1]
                triangle.append([1])
                for j in range(i-1):
                    triangle[-1].append(prev_array[j] + prev_array[j+1])
                triangle[-1].append(1)
    return triangle

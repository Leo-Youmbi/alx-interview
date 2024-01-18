#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """Calculate the minimum number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations. If n is impossible to achieve,
        return 0.
    """
    if n == 1:
        return 0

    operations = 0
    min_operation = 2

    while n > 1:
        while n % min_operation == 0:
            n //= min_operation
            operations += min_operation
        min_operation += 1

    return operations

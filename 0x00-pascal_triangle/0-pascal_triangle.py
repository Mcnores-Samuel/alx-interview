#!/usr/bin/python3
"""This module contains a function that returns a list of lists
representing the Pascal's triangle of a given size.

Example:
    pascal_triangle(5) returns:
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def calculate_pascal_bionomial_coefficient(n, k):
    """Calculates the binomial coefficient of n and k.

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose from the total.

    Returns:
        int: The binomial coefficient of n and k.
    """
    if k == 0 or k == n:
        return 1
    return calculate_pascal_bionomial_coefficient(n - 1, k - 1) + \
        calculate_pascal_bionomial_coefficient(n - 1, k)


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle of size n.

    Args:
        n (int): The size of the Pascal's triangle to generate.

    Returns:
        list: A list of lists representing the Pascal's triangle of size n.
    """
    if n <= 0:
        return []
    return ([[calculate_pascal_bionomial_coefficient(i, j)
              for j in range(i + 1)] for i in range(n)])

#!/usr/bin/python3
"""Island perimeter module. This module contains a function that calculates the
perimeter of an island in a 2D grid.
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a 2D grid.

    Args:
        grid (list of list of int): A 2D grid of 0s and 1s.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom neighbor
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right neighbor
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter

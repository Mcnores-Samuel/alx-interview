#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0

    operations_count = 0
    current_count = 1
    clipboard_count = 0

    while current_count < n:
        if clipboard_count == 0:
            clipboard_count = current_count
            current_count += clipboard_count
            operations_count += 2
        elif (n - current_count) % current_count == 0:
            clipboard_count = current_count
            current_count += clipboard_count
            operations_count += 2
        else:
            current_count += clipboard_count
            operations_count += 1

    return operations_count

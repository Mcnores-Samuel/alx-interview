#!/usr/bin/python3
"""This module contains a function that determines if a given data set
represents a valid UTF-8 encoding.

Example:
    validUTF8([197, 130, 1]) returns True
    validUTF8([235, 140, 4]) returns False
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): The data set to validate.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
        False otherwise.
    """
    bytes = 0
    for char_rep in data:
        mask = 1 << 7
        if not bytes:
            while mask & char_rep:
                bytes += 1
                mask = mask >> 1
            if not bytes:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if char_rep >> 6 != 0b10:
                return False
        bytes -= 1
    return bytes == 0

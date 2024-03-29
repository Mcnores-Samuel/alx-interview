"""This module reads stdin line by line and computes metrics,
printing them to stdout after every 10 lines read.
"""
import sys


def print_stats(status_codes, file_size):
    """Prints the computed metrics to stdout.

    Args:
        status_codes (dict): A dictionary containing status codes and their
            frequency.
        file_size (int): The total file size of the input.
    
    Returns:
        None
    """
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))
    return


def main():
    """Reads stdin line by line and computes metrics,
    printing them to stdout after every 10 lines read.

    Raises:
        KeyboardInterrupt: Raised when the user presses Ctrl+C.

    Returns:
        None
    """
    status_codes = {}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            split_line = line.split()
            try:
                file_size += int(split_line[-1])
            except Exception:
                pass
            try:
                status_code = int(split_line[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
            except Exception:
                pass
            if line_count % 10 == 0:
                print_stats(status_codes, file_size)
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise KeyboardInterrupt
    return


if __name__ == "__main__":
    main()
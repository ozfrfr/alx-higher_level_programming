#!/usr/bin/python3

"""Print a square of '#' characters.

This function prints a square made up of '#' characters with a specified size.

Args:
    size (int/float): The number of '#' characters to print.
                      Must be an integer or a non-negative float.

Returns:
    None: The function doesn't return a value, but it prints the square.
    Exception: If an exception occurs, the raised exception is returned.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is negative or a negative float.
"""
def print_square(size):
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, float) and size < 0:
            raise ValueError("size must be an integer")
        else:
            for row in range(size):
                for column in range(size):
                    print("#", end="")
                print()
    except Exception as e:
        return (e)


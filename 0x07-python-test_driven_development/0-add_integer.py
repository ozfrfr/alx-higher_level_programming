#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer (default is 98 if not provided).

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.

    This function takes two integer inputs, 'a' and 'b', and returns their sum. 
    If 'a' or 'b' is not an integer, it raises a TypeError.
    If 'a' or 'b' is a float, it converts them to integers before adding them.
    """
    try:
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            if isinstance(a, float) or isinstance(b, float):
                return int(a) + int(b)
            return a + b
    except Exception as e:
        return e


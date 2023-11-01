#!/usr/bin/python3

"""Print the first and last name and perform various tests for validation"""


def say_my_name(first_name, last_name=""):
    """Generate a formatted name string.
    Args:
        first_name (str) -> The first name.
        last_name (str) -> The last name.
    Returns:
        A string in the format 'My name is <first_name> <last_name>'.
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        else:
            return ("My name is {} {}".format(first_name, last_name))
    except Exception as ex:
        return (ex)


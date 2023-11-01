#!/usr/bin/python3

"""Text indentation formatter.

This function takes a text input and formats it with proper indentation rules.

Args:
    text (str): The input text to be formatted.

Returns:
    None: The function doesn't return a value, but it prints the formatted text.
    Exception: If an exception occurs, the raised exception is returned.

Raises:
    TypeError: If text is not a string.
"""
def text_indentation(text):
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        else:
            c = 0
            while c < len(text) and text[c] == ' ':
                c += 1
            while c < len(text):
                print(text[c], end="")
                if text[c] == "\n" or text[c] in ".?:":
                    if text[c] in ".?:":
                        print("\n")
                    c += 1
                    while c < len(text) and text[c] == ' ':
                        c += 1
                    continue
                c += 1
    except Exception as exc:
        return (exc)


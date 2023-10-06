#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module"""
    try:
        import hidden_4
    except ImportError:
        print("Error: Unable to import hidden_4 module.")
    else:
        names = dir(hidden_4)
        for name in names:
            if not name.startswith("__"):
                print(name)


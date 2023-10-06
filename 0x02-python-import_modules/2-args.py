#!/usr/bin/python3
import sys

# Get the number of command-line arguments (including the script name)
num_args = len(sys.argv) - 1  # Subtract 1 for the script name itself

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))

if __name__ == "__main__":
    pass

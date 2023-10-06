#!/usr/bin/python3
import sys

# Initialize a variable to store the sum of arguments
sum_of_arguments = 0

# Loop through command-line arguments starting from the second one
for arg in sys.argv[1:]:
    # Convert the argument to an integer and add it to the sum
    sum_of_arguments += int(arg)

# Print the sum of all arguments
print(sum_of_arguments)

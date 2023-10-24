#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0  # Variable to keep track of the number of elements printed

    try:
        for i, item in enumerate(my_list):
            if i < x:  # Print only if the index is less than x
                print(item, end='')
                printed += 1
        print()  # Add a newline after printing all elements

    except TypeError:
        print("An error occurred while printing")

    return printed

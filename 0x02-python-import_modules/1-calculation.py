#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
result = add(a, b)
formatted_string = "{} + {} = {}".format(a, b, result)
print(formatted_string)

a = 10
b = 5
result = sub(a, b)
formatted_string = "{} - {} = {}".format(a, b, result)
print(formatted_string)

a = 10
b = 5
result = mul(a, b)
formatted_string = "{} * {} = {}".format(a, b, result)
print(formatted_string)

a = 10
b = 5
result = div(a, b)
formatted_string = "{} / {} = {}".format(a, b, result)

if __name__ == "__main__":
    pass

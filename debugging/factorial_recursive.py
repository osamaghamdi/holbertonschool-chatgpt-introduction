#!/usr/bin/python3
import sys

"""
Calculate the factorial of the given number

param n: The number for which to calculate the factorial. It should be a non-negative integer

return: The factorial of the input number (n!), or 1 if n is 0
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

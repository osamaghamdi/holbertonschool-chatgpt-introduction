#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))
    print(f)
else:
    print("Please provide a number as an argument.")

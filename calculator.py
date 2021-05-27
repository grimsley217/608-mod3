#calculator.py
"""This calls various MATH functions."""

import math

x=int(input('Enter a value to take the SQUARE ROOT of: '))
y=float(input('Enter a value to calculate the FLOOR of: '))

a=math.sqrt(x)
b=math.floor(y)

print(f'The square root of {x} is {a}.')
print(f'The floor of {y} is {b}.')

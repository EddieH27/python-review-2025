"""
Fix the Errors #2 — Input & Math
"""
# x = input("Enter a number: ")
# y = input("Enter another number: ")
# print(f"Sum: {x + y}")
# age = input("How old are you?")
# print("In 10 years you will be {age} + 10")
# n = float(input("Enter a numerator: "))
# d = float(input("Enter a denominator: "))
# result = n / d
# print(f"Result: {result}")
# a = 5; b = 2
# print(f"Power: {a ^ 2}")
# print(f"Remainder: {a // b}")
# pi = 3.1415926535
# print(f"Pi is approximately {pi}")
x = 1
y = 2
z = 3
result = (x + y) * z - (y / x)
print(f"Result: {result}")
print(f"Division: {y/x}")
print(f"Addition: {x+y}")
print(f"Subtraction: {x-y}")
print(f"Modulo: {y%x}")
print(f"power: {x**y}")
print(f"Absolute value: {abs(x-y)}")
print(f"Max: {max(x,y,z)}")
print(f"min: {min(x,y,z)}")
pi = 3.1415926535
print(f"Round; {round(pi)}")
from math import *
print(f"square root of 16: {sqrt(16)}")
print(f"ceiling of Pi: {ceil(pi)}")
print(f"Floor of Pi: {floor(pi)}")
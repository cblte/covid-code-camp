# -*- coding: utf-8 -*-

"""Covid19 Code Camp
   Day 03 - Activity Task
"""
__author__ = "cblte "



print("---- Part A):")
x = 10
while x <= 20:
    print(x)
    x = x + 1


print("---- Part B):")
x = 100
while x > 0:
    print(x)
    x = x - 5

print("----  Part C):")
x = 1
while x <= 100:
    if x % 2 == 0:
        print("x")
    else: 
        print(x)
    x = x + 1


print("---- Part D):")
x = 5
manyX = []
while x <= 25:
    manyX.append(x)
    x = x + 5
print(manyX)  # looked up join in the documention. creates a string out of an array



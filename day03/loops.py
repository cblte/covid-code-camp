# -*- coding: utf-8 -*-

"""Covid19 Code Camp
   Day 03 - Lists and Tuples with a while loop 
"""
__author__ = "cblte "

towns =[]
x = ""

while x != "XXX":
    x = ""
    print("Enter a dutch town or XXX to quit")
    x = raw_input()
    if x != "XXX":
        print(x + " added to the list")
        towns.append(x)

print("You added the following towns to the list:")
for town in towns:
    print(town)


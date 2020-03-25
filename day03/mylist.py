# -*- coding: utf-8 -*-

"""Covid19 Code Camp
   Day 03 - Lists and Tuples
"""
__author__ = "cblte "


family = ["Carsten", "Sarah", "Grumpy", "Mareike", "Andre", "Werner", "Gaby"]

computer = ("Commodore 64", "Commodore 128", "Mac + ", "Atari 400", "Ibm Pc Jr.")

print("The complete array and tuple")
print(family)
print(computer)
print("-----")

family[0] = "Stefan"
# computer[0] = "Amiga"     #updating a tuple is not allowed

print(family[0])
print(family[1])
print(computer[0])
print(computer[3])

print(family[0:2])
print("-----")
print("")

# manipulating lists
family.append("Emma")
family.remove("Grumpy")
family.insert(0, "Christian")
print(family)

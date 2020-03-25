#!/usr/local/bin/python3
# -*- encoding: utf-8 *-*
# FW code camp day 02

import sys

value1 = int(sys.argv[1])
value2 = int(sys.argv[2])

if(value1 > value2):
    print("The first paramater is larger.")
elif (value2 > value1):
    print("The second parameter is larger.")
else:
    print("The parameters are equal")

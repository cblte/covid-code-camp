#!/usr/local/bin/python3
# -*- encoding: utf-8 *-*
# FW code camp day 02

import sys

age = int(sys.argv[1])
if (age >= 18):
    print("You are eligable to vote.")
    print("Please enter voting booth.")
else:
    print("No, You may not proceed. Not old enough to vote.")
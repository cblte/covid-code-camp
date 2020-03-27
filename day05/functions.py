# -*- encoding: utf-8 -*-
# 
# code camp day
#
# title: its all about functions

def greetMe():
    "This function provides a greeting"
    print("Hello, World. Greetings.")

# greetMe()
# greetMe()

def howMany(iters):
    "This function will print a number of Xs based on value passed in"
    x = 0
    while x < iters:
        print("X")
        x += 1  # increment x

# howMany(5)

def battingAverage(atBats, hits, walks):
    "Calculate average batting by providing the amount of bats, the hits and the walks"
    # need to cast hits to float before calculation starts
    average = float(hits) / (atBats-walks)
    print("Batting Average: %4.3f" % (average))     # using a formatting statement here

#atBats = input("At bats: ")
#hits = input("Hits: ")
#walks = input("Walks: ")

#battingAverage(atBats, hits, walks)
   

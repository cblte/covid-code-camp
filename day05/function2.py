# -*- encoding: utf-8 -*-
# 
# code camp day 05
#
# title: all about funtions part 2


def battingAverage(atBats, hits, walks):
    "Calculate average batting by providing the amount of bats, the hits and the walks"
    # need to cast hits to float before calculation starts
    average = float(hits) / (atBats-walks)
    # print("Batting Average: %4.3f" % (average))     # using a formatting statement here
    return average


def sluggingAverage(totalBases=1, atBats=1):
    sluggingAverage = float(totalBases) / atBats
    # print("Slugging Average: %4.3f" % (sluggingAverage))
    return sluggingAverage


atBats = input("At Bats: ")
totalBases = input("Total Bases: ")
hits = input("Hits: ")
walks = input("Walks :")

ba = battingAverage(atBats, hits, walks)
sa = sluggingAverage(totalBases, atBats)

print("The batting average is %4.3f and the slugging average is %4.3f." % (ba, sa))



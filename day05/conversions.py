# -*- encoding: utf-8 -*-
# 
# code camp day 05
#
# title: all about functions
# activity: converting fahrenheit to celsius and back, as well as km and miles


def convertTemp(temp, which = "c"):
    """Convert between fahrenheit and celcius
    temp first temp value
    which set to f to convert to fahrenheit, anything else will convert to celsius
    """

    if which == "f":
        return (temp * 9.0/5.0) + 32.0
    else: 
        return (temp - 32.0) * 5.0/9.0


def convertDistance(distance, which = "km"):
    """Convert between kilometer and miles
    distance is the distance you want to convert
    which set to m to convert kilometers to miles, anything else will convert to kilometers
    """

    if which == "m":
        return distance / 1.609
    else:
        return distance * 1.609

fh = convertTemp(60,"f")
cel = convertTemp(60, "c")

print("60 deg Celsius are in Fahrenheit: %4.2f" % (fh))
print("60 deg Fahrenheit are in Celsius: %4.2f" % (cel))

km = convertDistance(75,"km")
miles = convertDistance(km,"m")

print("75 miles are in kilometer: %4.3f" % (km))
print(str(km) + " kilometer are in miles: %4.3f" % (miles))

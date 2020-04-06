# -*- encoding: utf-8 -*-
# 
# code camp day 07
#
# title: more about classes


class Vehicle:

    numVehicles = 0

    def __init__(self, color, weight, numDoors, topSpeed, currentSpeed):
        self.color = color
        self.weight = weight
        self.numDoors = numDoors
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.__class__.numVehicles += 1

    def makeSound(self):
        print("brummm")

    
    def accelerate(self):
        if(self.currentSpeed < self.topSpeed):
            self.currentSpeed += 1
        return self.currentSpeed

    
    def brake(self):
        if(self.currentSpeed > 0):
            self.currentSpeed -= 1
        return self.currentSpeed


# ---------- end of class Vehicle

class Ambulance(Vehicle):
    def makeSound(self):
        print("taa tüü tataaa")

# ---------- end of class Ambulance




# ---------- start of program
carstensCar = Vehicle("raceblue", 1800, 5, 220, 0)
carstensCar.makeSound()
#sarahsCar = Vehicle("gray", 1400, 3, 175, 0)
#sarahsCar.makeSound()
#elosCars = Vehicle("beige", 2000, 5, 230, 0)
#elosCars.makeSound()
print("Number of vehicles: " + str(Vehicle.numVehicles) )

myAmb = Ambulance("white", 5000, 3, 130, 0)
print("Color of the ambulance vehicle: " + myAmb.color)
myAmb.accelerate()
myAmb.accelerate()
myAmb.accelerate()
myAmb.makeSound()
print("The ambulance is now moving at " + str( myAmb.accelerate() ) + " km/h")

print("Number of vehicles: " + str( Vehicle.numVehicles) )






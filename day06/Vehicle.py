# -*- encoding: utf-8 -*-
# 
# code camp day 06
#
# title: learning about classes

class Vehicle:
    def __init__(self, make, model, color, weight, numDoors, topSpeed, currentSpeed):
        self.make = make
        self.model = model
        self.color = color
        self.weight = weight
        self.numDoors = numDoors
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
    
    def accelerate(self):
        """Accelerate by 5 if still below topSpeed
        """
        if self.currentSpeed < self.topSpeed:
            self.currentSpeed += 5
        if self.currentSpeed >= self.topSpeed:
            self.currentSpeed = self.topSpeed   # cannot go higher than topspeed
            print("Can't go faster. Top speed reached")
        return self.currentSpeed


    def brake(self):
        """step on the brake and reduce speed by 5 if not already stopped
        """
        if self.currentSpeed > 0:
            self.currentSpeed -= 5
        if self.currentSpeed < 5:
            self.currentSpeed = 0
        return self.currentSpeed


    
carstensCar = Vehicle("Skoda", "Octavia", "Race Blue", 1800, 5, 229, 0)
sarahsCar = Vehicle("Volkswagen", "Polo", "Gray", 1400, 3, 180, 0)
golfCar = Vehicle("Melex", "EC21", "White", 360, 0, 25, 0)

print(carstensCar.make + " " + carstensCar.model)
print(sarahsCar.make + " " + sarahsCar.model)
print(golfCar.make + " " + golfCar.model)

carstensCar.currentSpeed = 220
carstensCar.color = "Racing Blue"

carstensCar.accelerate()
print("The " + carstensCar.color + " colored car is driving " + str(carstensCar.currentSpeed) + "km/h")
carstensCar.accelerate()
print("The " + carstensCar.color + " colored car is driving " + str(carstensCar.currentSpeed) + "km/h")

print("")
print("Accelerating with the GolfCar")
while golfCar.currentSpeed < golfCar.topSpeed:
    golfCar.accelerate()
    print("Golf car now at " + str(golfCar.currentSpeed))

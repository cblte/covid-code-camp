
grades = { "Mark" : 84, 
        "Donna" : 90,
        "Claire" : 82,
        "Murray" : 71,
        "Connor" : 80,
        "Neil" : 100,
        "Jenny" : 61 
        }

#print(grades)

# changing a value of an key
grades["Mark"] = 91

# adding new things or updating existing once
grades.update({"Sammie": 32})
grades.update({"Petunia": 99})
grades.update({"Mark": 44})

print("Mark: " + str(grades["Mark"]))
print("Sammie: " + str(grades["Sammie"]))
print("Petunia: " + str(grades["Petunia"]))
#print(grades["Bryan"])

# deleting entries
# del grades["Mark"] - delete mark only
# grades.clear() - clears the object
# del grades - deletes the object

print(grades)
del grades["Mark"]
print(grades)
grades.clear()
print(grades)
# del grades
# print(grades) # leads to an error



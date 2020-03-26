# -*- encoding: utf-8 -*-
# 
# looping through dictionaries
# ----------------------------

grades = { "Mark" : 84, 
        "Donna" : 90,
        "Claire" : 82,
        "Murray" : 71,
        "Connor" : 80,
        "Neil" : 100,
        "Jenny" : 61 
        }

print("Grades in the system:")
print(grades)
print("----------")

# looping through all items, a pair is returned
for student, grade in grades.items():
    print(student + " : " + str(grade))

# accessing all the values w/o the keys
total = 0
items = 0

for grade in grades.values():
    total = total + grade
    items = items + 1

average = total / items
print("The average grade is " + str(average))
print("----------")

print("Class List")
for name in grades:
    print(name)


    

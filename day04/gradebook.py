# -*- encoding: utf-8 -*-
# 
# looping through dictionaries
# 
# activity 002 of day04
# ----------------------------

# enter student names and grades to create a book of grades. exit by entering XXX

student = ""
gradebook = {}

print("Enter XXX to stop entering students")

while student != "XXX":
    student = raw_input("Name: ")
    if student != "XXX":
        grade = int(raw_input("Grade: "))
        gradebook.update({student: grade})


# running statistics
lowStud = ""
lowGrade = 9999 # set impossible high number as nobody can get this
highStud = ""
highGrade = 0
avarageGrade = 0
amountStudents = 0

print("You entered the following information about the students:")
for stud, grade in gradebook.items():
    print("Student < " + stud + " > has a grade of: " + str(grade))
    avarageGrade = avarageGrade + grade
    amountStudents = amountStudents + 1
    
    # find low and high
    if grade < lowGrade: 
        lowStud = stud
        lowGrade = grade
    if grade > highGrade:
        highStud = stud
        highGrade = grade


avarageGrade = avarageGrade / amountStudents
print("Avarage grade is: " + str(avarageGrade))
print("Student with highest Grade is: " + highStud + "("+ str(highGrade) + ")")
print("Student with lowest Grade is: " + lowStud + "("+ str(lowGrade) + ")")


# alternativ
maxStud = max(gradebook, key = lambda s: gradebook[s])
minStud = min(gradebook, key = lambda s: gradebook[s])

print("Student with highest Grade is: " + maxStud + "("+ str(gradebook[maxStud]) + ")")
print("Student with lowest Grade is: " + minStud + "("+ str(gradebook[minStud]) + ")")

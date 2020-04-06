# -*- encoding: utf-8 -*-
# 
# code camp day 007
#
# title: activity 001 - Employee class with childclasses ptEmployee and ftEmployee
#
# 


class Employee:
    """The Employee class representing an employeer with a 
        name, social security number (string) and in which 
        department that person works
    """
    
    empName = ""
    empSocial = ""
    empDepartment = ""

    def __init__(self, empName, empSocial, empDepartment):
        self.empName = empName
        self.empSocial = empSocial
        self.empDepartment = empDepartment

    def info(self):
        print("")
        print("----- Employee Information -----")
        print("Name______________: " + self.empName)
        print("Social Security #_: " + self.empSocial)
        print("Department_________ " + self.empDepartment)
        print("----- end of information block -----")

# ---------- end of Employee class


class ptEmployee(Employee):
    """PartTimeEmployee child class of Employee
        enhancing the employee with hourlyPay
    """
    hourlyPay = 0

    def __init__(self, name, social, department, hourlyPay):
        Employee.__init__(self, name, social, department)
        self.hourlyPay = hourlyPay

    def calculatePay(self, hoursWorked):
        """calculate payment based on hours worked."""
        payment = self.hourlyPay * hoursWorked
        return payment


# ---------- end of ptEmployee class


class ftEmployee(Employee):
    """FullTimeEmployee child class of Employee
        enhancing the employee with a yearlySalary
    """
    yearlySalary = 0
    
    def __init__(self, name, social, department, yearlySalary):
        Employee.__init__(self, name, social, department)
        self.yearlySalary = yearlySalary

    def calculatePay(self):
        """calculates payment based on 26 payment periods"""
        payment = self.yearlySalary / 26.0
        return payment

# ---------- end of ftEmployee class


# --------- programme starts

# mark works fulltime and gets 75.000 per year
mark = ftEmployee("Mark", "ss-mark-0987654321", "FrameWorkTV", 75000)
# carsten works part time only and makes 24.50 per hour
carsten = ptEmployee("Carsten", "ss-cars-3214569870", "CodeCampDesigner", 24.50)


mark.info()
print("Mark has a calculated payment of {:.2f} per period".format(mark.calculatePay()))

carsten.info()
print("Carsten has a calculated payment of {:.2f} per 40 hours".format(carsten.calculatePay(40)))

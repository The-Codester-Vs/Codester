# inheritance
import time
from functools import lru_cache

@lru_cache(maxsize=10)
def TimeTravel(n):
    time.sleep(2)
    return n

class Employee:
    def __init__(self,name,salaary,worktime):
        self.name = name
        self.salaary = salaary
        self.worktime = worktime
    def det(self):
        return f"The name of employee is {self.name}.\nThe salaary of the employee is {self.salaary} Rupees.\nThe total working time of employee is {self.worktime} hours."
class langauges:
    def __init__(self):
        self.websiteprogramming = []
        self.appdevelopment = []
        self.programminglanguages = []

class main(Employee,langauges):
    def details(self): 
        return f"The name of Employee is {self.name}.\nThe monthly income of Employee is {self.salaary}.\nWorkTime of employee is {self.worktime} hours.\nWebDevelopment languages which employee know  are {self.websiteprogramming}.\nAppDevelopment languages which employee know are {self.appdevelopment}.\nThe total programming languages which employee know are {self.programminglanguages}" 
# print("Share details with us")
_name = input("Enter Your Name: ")
_salaary = int(input("Enter Your monthly income in number: "))
_workTime = int(input("Enter Your working time in complany: "))
# _website = input("Enter WebDevelopment languages which you know: ")
# _app = input("Enter AppDevelopment languages which you know: ")
# _programming = input("Enter all Programing languages which you know: ")
print("Processing.",end ='')
time.sleep(0.50)
print(".",end = '')
time.sleep(0.50)
print(".")


TimeTravel(2)
("Done!")
TimeTravel(2)
# Employee_ = main(_name,_salaary,_workTime,_website,_app,_programming)   
harry = main(_name,_salaary,_workTime)       
print(harry.det())
import time
class codester:

    def __init__(self,name,age,hobbies,style):
        self.name  = name
        self.age = age
        self.hobbies = hobbies
        self.style = style

    def details(self):
        return f"Codester name is {self.name}.\nAge of the codester is {self.age} Year.\nHobbies of the Codester are {self.hobbies}.\nStyle of the Codester is {self.style}"

class information(codester):

    def __init__(self,Office_address,home_address):
        self.office_address = Office_address
        self.home_address = home_address

    def details_information(self):
        return f"Office Address of the codester {self.office_address}.\nHome address of the Codester {self.home_address}"

class main_platform(information):
    
    def total_details(self):
        return f"Codester name is {self.name}.\nAge of the codester {self.age}.\nHobbies of the Codester are {self.hobbies}.\nStyle of the Codester {self.style}\n--------------------------------------------\nOffice Address of the Codester {self.office_address}.\nHome address of the Codester {self.home_address}"


# time.sleep(1)
name = input("Enter your name: ")
age = int(input("Enter your Age: "))
HOBBIES = input("Enter your HOBBIES: ")
Style = input("Enter your style: ")
vivek  = codester(name,age,HOBBIES,Style)
print('Processing.',end = "")
time.sleep(2)
print('.',end ="")
time.sleep(1)
print('.')

print(vivek.details())
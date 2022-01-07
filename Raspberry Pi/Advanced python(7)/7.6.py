#Attributes of a class:
#1. Inheritance

class Person:
    """A class that defines the attributes of a person"""

    def __init__(self, first_name, last_name, gender,telephone):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender.lower()
        self.telephone = telephone
        self.email = first_name+"."+last_name+"@goo.com"


    def profile(self):
        print(self.first_name + " " + self.last_name + " is a " + self.gender + " and his phone number is " +str(self.telephone) )

print("The class Person is: " + Person.__doc__)



#Use inheritance to create a subclass of an
#existing class and add new member variables and methods.

class Employee(Person):
    def __init__(self, first_name,last_name,gender,telephone,salary):
        super().__init__(first_name,last_name,gender,telephone)
        self.salary = salary

    def give_raise(self, amount):
        self.salary = self.salary +amount

Jane = Employee("Jane,","Stone","Female", 323455,300)

Jane.profile()

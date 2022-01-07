#Defining a class Person :
#Functions that are associated with a particular class are called methods
class Person:
    """docstring for class Person"""

    def __init__(self, first_name, last_name, gender,telephone):
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.gender = gender

    def profile(self):
        print(self.first_name + " " + self.last_name + " is a " + self.gender + " and his phone number is " +str(self.telephone) )



Mike = Person("Micheal", "Simith","male", 123456)
Mike.profile()

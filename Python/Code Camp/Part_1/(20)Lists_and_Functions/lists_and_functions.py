#How to work with lists as an arguments
#How to work with lists inside of functions

def greet_all(people):
    for person in people:
        print("Connecting..." + person)

print("🥳Welcome to firends hangout call!")
print("In this app we connect you to your friends! 😀")

first_person = input("Enter the name of your first friend: ")
second_person = input("Enter the name of your second friend: ")
third_person = input("Enter the name of your third friend: ")


friends = [first_person,second_person,third_person]
greet_all(friends)
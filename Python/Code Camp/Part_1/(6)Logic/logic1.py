#branching

print("Hi! Welcome to Bazzu drinking")
print("What is you first name: ")
first_name = input()
print("What is your last name:")
last_name = input()

print("How old are you? ")
age = int(input())

if(age>=21):
    print("You are old enough to use this app.")
else:
    print("Sorry, you are not old enuogh to drink ;)")
    years = 21 - age
    print("Come back in " + str(years)+ " year(s)")
    print("Thanks for using our app!")

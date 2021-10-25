#We will be talking about functions that call other functions

def greetings(name, be_nice=True ): 
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"

def greet_all(people):
    for person in people:
            evaluation=  greetings(person) #Something is returned so it is good to save it to a variable
            print(evaluation)

friends = ["Jnae","Blan","Marinda"]

greet_all(friends)
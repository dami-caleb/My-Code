#Making keyword and position only parameters
def greetings(name,/, *, be_nice, ): # Adding a comma and a backslash after name makes "only name" position only. Anything after the "*" becomes a keyword only parameter (That means in our case "be_nice" has become a keyword only parameter) 
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"


print(greetings("Mike",be_nice=True))
#The first arguments is position only
#The second argumen t is name only
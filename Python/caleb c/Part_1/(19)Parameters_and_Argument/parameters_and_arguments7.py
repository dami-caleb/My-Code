#Keyword only parameters (passing parameters only by name )
def greetings(name, *, be_nice, ): #Anything after the "*" becomes a keyword only parameter (That means in our case "be_nice" has become a keyword only parameter) 
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"


print(greetings("Mike",be_nice=True))






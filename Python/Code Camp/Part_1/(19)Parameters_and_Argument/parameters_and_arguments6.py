#creating position only parameters

def greetings(name, be_nice, /):  #Adding a comma and a backslash makes it position sensitive
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"


print(greetings("Mike",True))

#print(greetings(be_nice=False,name="Jeff"))#This will not work


###########################################
#We can also try and make a particular argument position only
def greetings(name, /, be_nice, ):  #Adding a comma and a backslash after name makes "only name" position only.   (So everything before the backslah becomes position only)
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"


print(greetings("Mike",be_nice= True)) #This works
print(greetings("Ras", True)) #This also works
#################################################
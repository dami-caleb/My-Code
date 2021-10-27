#Properties of arguments
def greetings(name = "User", be_nice=True):  
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"


print(greetings(name="Jason", be_nice="True"))#This will work
print(greetings("Jason",False))#This will work
#print(greetings(False,"Lura")) #This will not work(Arguments are position sensitive to the parameter)
print(greetings(be_nice=False, name ="Jane")) #The reson why this will work is because (arguments are also name sensitive to the parameters) you called out the respective variable name that is in the parameter, in the argument

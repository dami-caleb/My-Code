#Passing less arguments to a numerous arguments function
def greetings(name = "User"):  #what we just did by puting "name" in the bracket AND ASIGNING IT THE STRING "User" is declearing a default parameter for the function (if no argument is recived)
    if name == "Claire":
        return "WOW! What's up Claire"
    return "Hello and welcome " + name + "!"

print(greetings("Caleb"))
 

 #####################
def greetings(name = "User", be_nice=True):  
    if not be_nice:
        return "Who do you think you are?"
    return "Hello and welcome " + name + "!"

#Now for the function above we have two parameters that menas we need two arguments
#But it is possible to input one argument and use the default parameter
#To do that we call out the parameter by name and assign the respective value to it. While the other one that is ommited (has no argument), will use the default Parameter
print(greetings(be_nice=False))

#return values
def greetings(name):  #what we just did by puting "name" in the bracket of the function definition "greetings" is known as a parameter
    if name == "Claire":
        return "WOW! What's up Claire"
    return "Hello and welcome " + name + "!"






#The way we pushed the  data(line of code) away is known as an abstraction, we have abstracted away the inner details by creating a function



user_name = input('Hi! What is your name: ')
returned_value = greetings(user_name)  #what we just did here whereby we passed in data is known as an argument
print(returned_value) 

##################################
#We can directly print instead of creating a variable, then printing that variable
#we could do:
#print(greetings(user_name))
#since we know a value will be returned
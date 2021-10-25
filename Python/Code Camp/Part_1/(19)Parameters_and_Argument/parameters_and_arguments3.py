#Default parameters
def greetings(name = "User"):  #what we just did by puting "name" in the bracket of the function definition "greetings" is known as a parameter. And assinging it a string "user" is known as creating a default parameter
    if name == "Claire":
        return "WOW! What's up Claire"
    return "Hello and welcome " + name + "!"

print(greetings())
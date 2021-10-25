#return
#This can be use dto exit a function early

def greetings(name):  #what we just did by puting "name" in the bracket of the function definition "greetings" is known as a parameter
    if name == "Claire":
        print("You smell like pickles")
        return 
    print("Hello amd welcome " + name + "!")

user_name = input('Hi! What is your name: ')
greetings(user_name)  #what we just did here whereby we passed in data is known as an argument



#######################
#"return" works in a similar way with "continue" and "break" with loops except we use it with functions
# "break" and "continue" can only be used for loops 

#we could have replaced the "return" in the greetings() function with a else but  "return" is already there so
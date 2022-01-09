#Error Handling

#If something goes wrong while a program is running,
#you may want to catch the error or exception
#and display something more friendly

#To do this we use the:
#try/except construct

try:
    user_input = input("Enter a number: ")
    print(user_input+4)
except IOError:
    print("What you enterd is not a number 😉")

# You can also have separate except sections for
#catching different types of exception
#If you do not specify any exception class,
#all exceptions will be caught by the except command.





#####################################
#Python also allows you to have else and finally clauses in
#your error handling:
list = [1, 2, 3]
try:
    list[8]
except:
    print("out of range")
else:
    print("in range")
finally:
    print("always do this")
######################################
#The else clause will be run if there is
#no exception, and the finally will be
#run whether there is an exception or

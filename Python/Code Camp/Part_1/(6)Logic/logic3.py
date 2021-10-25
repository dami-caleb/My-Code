print("What is your age")
age = int(input())
if age>20:
    print("Welcome to our app!")
elif age> 65:
    print("Hey, you get a special discount")

print("Thanks for using our app!")



#When using "elif" oder does matter
#eg.
print("What is your age")
age = int(input())
if age> 65:
    print("Hey, you get a special discount")
elif age>20:
    print("Welcome to our app!")
else:
    print("You are not old enough")

print("Thanks for using our app!")
#It only executes the first condition that is true
###################################
#Note:
#"elif" does not depend on the "if"
# statement.
# only the "else" statement that does
######################################

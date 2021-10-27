#logical operator
#"or" = one or both of the operands can be true


print("What is your name? ")
user_name = input()
if (user_name=="Caleb" or user_name=="Ally"):
    print("Hi")

#################################
#short circuit:
#This is when python checks a comparison ("or") and executes if only one part of the comparison is true

if True or print("Hi"):
    print("Hello")

if False or print("Hi"):
    print("Hello")


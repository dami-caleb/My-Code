from random import randint #we can decide to use one function of a module (we are using the function randint from the random module)

print(randint(0,10))   #The got you there is you can only use that function of the module,you can not use any other function that module has. You can only access the individual ones you import directly
                   # if you want to access any other function from the module  you have to import it has well

#the advantage here is you don't have to prefix with the module name
#you can use he function directly
#The disadvantage here is you can only use the imported function from the module
#and no other function from that module (unless you import it aswell)
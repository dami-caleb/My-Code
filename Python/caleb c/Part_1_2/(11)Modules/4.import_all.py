#importing every function from a module

print(dir())
print()

from random import * #the problem here is the problem we disscused in prevous examples (the naming of variables)
                     #our identifier list has now increased
print(dir())

#we can not name our variable the name of a function from the imported variable
#so we have to know all the function names that have been imported to aviod giving a varaible the name


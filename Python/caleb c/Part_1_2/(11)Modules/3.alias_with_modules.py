#Introduction to alaisis with modules

#To fix the problem disccused in 2.module.def
#we create an alias

#for example we need to use the variable name math

import math as m #now we use the variable name math. And if we want to use a function from the math module we use the alias module
math = 43
result= m.sqrt(34)
print(result)

from random import randint as r
randint = 566666 #now we can use randint as a variable name
print(r(0,randint)) #and if we want to use the function randint we use the alias r



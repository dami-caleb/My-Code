##The problem with import is it has the potential to overide a variable you have already created
##So it is good to always decleare your import before you write your code 

##for example
math =3
import math
print(math) #prints the location of the module math

math =3 
#math.sqrt(32) #this can not work because variable math has replaced the module math
print(math)
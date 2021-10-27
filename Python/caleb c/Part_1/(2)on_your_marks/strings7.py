#Nested fuction calls
import math

age = 17

print(len(str(id(str(age)) + math.floor(2.6))))

#The thing in the ineermost bracket happen first

##
""" 
print(str(age))
print(id(str(age)))
print(str(id(str(age))))
"""
print(len(str(id(str(age)))))
print(round(2.6))

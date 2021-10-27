#Copying a lists
#There are two ways

stuff = ["Learn", 12, "Fun", ['CODE','PROGRAMING', 'GOING TO THE GYM']]

copy_of_stuff = stuff[:]

copy_of_stuff[0] = "Study"

print(stuff, copy_of_stuff)
#notice how we changed "copy_of_stuff" and it did not affect "stuff" 



""" Another way of copying a list it is by adding ".copy()" """
another_way_of_copying_a_list = stuff.copy()
another_way_of_copying_a_list[3] = "Computing"
print(stuff, another_way_of_copying_a_list)
""" Notice how changing one thing in the copy does not affect the original """
#The "." makes it possible to attach a function to an object(another_way_of_copying_a_list)
#It is called a dot operator and it is how we can grab functions for a particular object
#Functions attached to objects are known as methods
"""Note: This way of copying a lists is called a shallow copy"""






#############################################################
#Note, doing:
#copy_of_stuff = stuff
#is not making a copy
#why?
#because if you change one thing in "copy_of_stuff" it will also change it in "stuff"
#What "copy_of_stuff = stuff" does is making an allias
copy = stuff
copy[1] = "3"
print(stuff,copy)
#Notice how changing what is in "copy" also changes what is in "stuff", therefore THIS IS NOT A COPY BUT AN ALIAS
#############################################################
#This same problem happens if you use a shallow copy in a two dimentional (nested) list

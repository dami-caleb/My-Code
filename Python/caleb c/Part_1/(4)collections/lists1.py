#Unlike strings lists are mutable (This means you can use indexes to change the things in a list)
ages = [12, 45, 2]
#list of integers
 
people = ["Mark", "class", "James"]
#list of strings

stuff = ["Learn", 12, "Fun", ['CODE','PROGRAMING', 'GOING TO THE GYM']]
#list of a mix of data types

###########################################################
stuff[1] = 2
print(stuff)
print(id(stuff))

stuff[3] = "Computer science"
print(stuff)
print(id(stuff))    #same memory address, no new memeory was created (we just changed the data in that memeory. This is what strings can't do) 

#We changed the data and we did not create a new object in memeory it is still pointing to the same object in memeory
#we just changed the data inside the lists
#############################################################

stuff[1] = "Happy"
print(stuff)        #so we can replace an "integer" with a "string" in lists
############################################################

print("The length of the list (how many things are in the lists) stuff is " + str(len(stuff)))

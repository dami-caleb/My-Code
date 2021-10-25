#lists comprehension and sets
#We are going to count the number of items in a lists using "set"

backpack = ["sword","rubber duck","slice of pizza","parachute","sword","sword"]

number_of_items = [backpack.count(item) for item in set(backpack)]   #the "set()" is there because,  it will give us the output that we  want
print(number_of_items)

number_of_items = [[backpack.count(item), item] for item in set(backpack)]
print(number_of_items)

##################
# if you don't want to put the result in a list 
[print(backpack.count(item), item) for item in set(backpack)]



########################################
#A simple way of counting the things in a lists is by using the function "counter"
#You first have to import the library

from collections import Counter

print(Counter(backpack))         #This is a dictionary.
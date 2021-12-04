#Dictionaries are data structure to hold numerous elements
#The difference is in dictionaries there is an accociation of two elements

emails = {
    "james":"james@email.com",   #The name on the left (james) is called the key
    "jane":"jane@email.com"     #The email on the right is called the value 
}

number = {
    "james": 1323445555,
    "jane": 3244555555
}

print(emails)
print(number)


#The key has to be a value that is hashable
#hashable means the data can be converetd to a number

Pass = {"James":True, "Jane":False}
print(Pass)

print(hash(True))  ##see true can be hashable

#dictionaries don't work with mutable types 
#A tuple is like a string, but it is not mutable

#mutable =  the data can be changed

#Advantage:
#No matter the size of a dictionary, the time taken to retrive data does not increase
#You can accociate two data together
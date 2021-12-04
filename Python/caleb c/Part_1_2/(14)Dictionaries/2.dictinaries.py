#Dictionaries are data structure to hold numerous elements
#The difference is in dictionaries there is an accociation of two elements

emails = {
    "james":"james@email.com",   #The name on the left (james) is called the key
    "jane":"jane@email.com"     #The email on the right is called the value 
}

numbers = {
    "james": 1323445555,
    "jane": 3244555555
}


####How to retrive data from a dictionary
# using email[index] does not work

print(emails["james"])

#To avoid error, we can check to see if the data exist
if "jane" in numbers:
    print(numbers["jane"])
    
    
################################################
#A better way of getting data from a dictionary is using a method
print(emails.get("jane"))
#if the data you are looking for is not in the dictionary "None" is printed
#you can also decide what will be printed out if the data is not found
print(emails.get("jANE","THIS DATA IS NOT IN THE DATA BASE"))

#iterating through the keys of a dictionary
emails = {
    "james":"james@email.com",   #The name on the left (james) is called the key
    "jane":"jane@email.com"     #The email on the right is called the value 
}

for k in emails:
    print(k)

#iterating through the values of a dictionary
for elem in emails.items():
    print(elem)
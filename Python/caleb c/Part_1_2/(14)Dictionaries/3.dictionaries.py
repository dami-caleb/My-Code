#inserting data to a dictionary

emails = {
    "james":"james@email.com",   #The name on the left (james) is called the key
    "jane":"jane@email.com"     #The email on the right is called the value 
}

emails

emails["kelvin"] = "kelv@gmail.com"
print(emails)

emails.update({"jef":"jef@email.com", "rayan":"rayan@mail.com"})
print(emails)

emails.update(rex="rex@gmail.com")
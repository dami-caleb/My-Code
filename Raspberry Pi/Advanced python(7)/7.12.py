#Using regular expressions to validate
#data entry

import re

regex = '^[‘\w_\.+-’]+@[\w_\.-]+\.[\w_-]+$'

print("Welcome to the emf portal.")
while True:
    user_email = input("Kindly enter your email address to login: ")
    if re.search(regex, user_email):
        print("Your portal is loading.")
    else:
        print("Wrong email address, please try again.")

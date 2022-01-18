#Using regular expressions to validate
#data entry

import re

username_regex = '^[‘\w_\.+-’]+@[\w_\.-]+\.[\w_-]+$'
password_regex = '^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$'  #requires at least one special character

wrong_login_details = True

while wrong_login_details:
    print("Welcome to the emf portal.")
    user_email, user_password = input("Kindly enter your email address to login: "), input("Enter your password: ")

    print("Processing......")
    if re.search(username_regex, user_email) and re.search(password_regex,user_password):
        print("Your portal is loading.")
        wrong_login_detailscondition = False
    else:
        print("Wrong email or password entered, please try again.")

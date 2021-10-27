#An indefinite(or sentinel) loop is an infinite loop that can be broken out of if a condition is met
while True:
    print("Processing... Enter \"Q\" to quit prosessing")
    user_response = input()
    if user_response == "Q":
        break
    else:
        print("Incorrect input")




#A sentinel value is a value used to stop a loop.
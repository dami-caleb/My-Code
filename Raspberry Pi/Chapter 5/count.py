mangoes = 10

print("Welcome to the mango dispenser.")
Welcome_screen = "How many magoes do you want?"
print(Welcome_screen)

user_input = int(input("Enter number: "))

if (user_input>mangoes):
    print("The number of mangoes you want is more than the number of mangoes we have")
    too_much_screen = print("Do you want to see the number of mangoes you can take? ")
    user_input1 = input("Enter Yes or No: ").lower()

    if(user_input1=="yes"):
        for mango in range(mangoes):
            print ("You can take",mango,"mangoes")
    else:
        print("Goodbye!")
else:
    remaining = mangoes - user_input
    print("You have ", remaining, "mangoes remaining")

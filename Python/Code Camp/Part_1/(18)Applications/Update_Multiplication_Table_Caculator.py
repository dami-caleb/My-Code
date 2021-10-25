def multiplication_table():
    print("Welcome to the multiplication table provider :)")

    multiplication_table = int(input("Kindly enter the multiplication table you would like to see: "))
    end_of_table = int(input("Where will you like to end the multiplication table: "))

    i = 0

    while i<= end_of_table:
        result = multiplication_table*i
        print(str(multiplication_table)+ "*" +str(i) + " = " + str(result))
        i +=1

multiplication_table()
print("Would you like to see another multiplication table? ")
user_response = input("Yes or No: ")

while user_response.lower() == "yes":
    multiplication_table()
    print("Would you like to see another multiplication table? ")
    user_response = input("Yes or No: ")
else:
    print("Thank for using our app! :) ")


i=0
max_number = 405


print(" Welcome to the guessing game!")
print("You will be asked to enter five(5) numbers")
print("If one of the numbers you entered squared, is larger than the systems number, you win! :)")
print("Let's begin! ;)")

first_number = int(input("Kindly enter the first number: "))
second_number = int(input("Kindly enter the second number: "))
third_number = int(input("Kindly enter the third number: "))
fourth_number = int(input("Kindly enter the fourth number: "))
fifth_number = int(input("Kindly enter the fifth number: "))

list_of_numbers = [first_number, second_number, third_number, fourth_number, fifth_number]

while i < len(list_of_numbers):
    if list_of_numbers[i] ** 2 < max_number:
        print(list_of_numbers[i], "squared is less than the systems number")
    else:
        print("Hurray!",list_of_numbers[i], " squared is greater than the systems number!")
        print("You win!")
        break
    i +=1




def healthy_food_checker(food):
    healthy_foods__lists =["almonds","nuts","lentils","oatmeal","wheat","broccoli","apple","kale","blueberries","avocados","vegetables","potatoes","fish","chicken","eggs"]      #https://www.medicalnewstoday.com/articles/245259#Fish,-meat,-and-eggs
    if food  not in healthy_foods__lists:
        bad_result = "🤔This food is not in our healthy food list."
        return bad_result
    else:
        good_result = "Yes!🥳 This food is healthy 😉"
        return good_result

print("😊Welcomne to the healthy food checker app! 😄")
print("The purpose of this app is to encourage healthy eating in people.")
print("Enter the name of the food you are about to eat or cook, and we will check if it is healthy or not.")

user_input = input("Enter: ")
result = healthy_food_checker(user_input.lower()) #We called the healthy_food_checker_function. And used the user input in lower case as the argument
print(result)

print("Do you want to check any other food?")
check_again = input("\"Yes\" or \"No\": ")

while check_again.lower() == "yes":
    print("Enter the name of the food you are about to eat or cook, and we will check if it is healthy or not.")
    user_input = input("Enter: ")
    result = healthy_food_checker(user_input.lower())
    print(result)
    print("Do you want to check any other food?")
    check_again = input("\"Yes\" or \"No\": ")
else:
    print("Thanks for using our app 😊")

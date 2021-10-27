#we use flags to check if a condition has been meet
#A  flag is a boolean or integer to indicate if something happened or a condition has been meet

numbers = [200, 30, 400 ,500 ,6]
 

i = 0
square = 500

while i < len(numbers):
    if numbers[i] ** 2 >square:
        print(numbers[i], "squared is larger than", square)
        break
    print(numbers[i], "squared is not larger than", square)
    i += 1
else:
    print("None squared are larger than", square)













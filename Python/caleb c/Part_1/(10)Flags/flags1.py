numbers = [20, 3, 4 ,0 ,6]
 

i = 0
square = 500
success  =False

while i < len(numbers):
    if numbers[i] ** 2 >square:
        print(numbers[i], "squared is larger than", square)
        success = True
        break #we could have kept a else statement here. But because of the "break" statement it is not neccessary
    print(numbers[i], "squared is not larger than", square)
    i += 1

if not success:
    print("None squared are larger than", square)


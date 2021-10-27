#the "else" statement (clause) combined with the while loop

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




#The same can also be done with a "for" loop
for number in numbers:
    if number**2 >square:
        print(number, "is greater than computers value")
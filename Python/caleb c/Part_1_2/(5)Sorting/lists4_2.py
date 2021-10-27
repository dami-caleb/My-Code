numbers = [2,1,3,55,76,32,12,21,32,20]

#Homework: Print the elements in the list "numbers" in reverse

#solution_1
numbers.sort()
numbers.reverse()

print(numbers)




numbers = [2,1,3,55,76,32,12,21,32,20]

#solution_2
#using the "sorted()" function
result = sorted(numbers, reverse=True)  #what this does is; (1.)It sorts the elements in the list. (2.) It reverse the sorted elements 
print(result)


#creating_a_function_that_revers_a list



############################
#swaping elements in a list

data = ["a","b","c","d","e","f","g"]


"""

index = 0




data[index], data[index-1] = data[index-1], data[index]

data[index+1], data[index-1-1] = data[index-1-1], data[index+1]

data[index+1+1], data[index-1-1-1] = data[index-1-1-1], data[index+1+1]

print(data)
"""



index = 0

mid_point = (len(data)-1)//2

while index < mid_point:
    data[0+index], data[-(index+1)] = data[-(index+1)], data[0+index]
    index+=1

print(data)


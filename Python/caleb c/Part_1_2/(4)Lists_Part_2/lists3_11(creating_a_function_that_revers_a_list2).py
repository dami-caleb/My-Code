#creating_a_function_that_revers_a list


data = ["a","b","c","d","e","f","g"]

for index in range((len(data)//2)):
    data[index], data[-index-1] = data[-index-1],  data[index]

print(data)
#creating_a_function_that_revers_a list

data = ["a","b","c","d","e","f","g"]
""" 
for item in reversed(data): ####what the function "reversed()" dies is to create a reversed iterator that starts from the back
    print(item)

"""


############################
# so we can use the "reversed()" function to create a function that reverse a list

storage = []

for item in reversed(data):
    storage.append(item)

print(storage)
print(data)
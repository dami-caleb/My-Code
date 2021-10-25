data = ["a","b","c","d","e","f","g"]

#we can put a step (the number after the last colon is a step(which is the amount we want to go each time) )

print(data[::2])#prints at 2 step

#using this to create _a_function_that_revers_a list
data[:] = data[::-1]
#lists comprehension syntax
squares = []

for i in range(10):
    squares.append(i**2)

print(squares)


####################################
#Another way of doing it
squares = [i**2 for i in range(10)]    #Notice that there is no if statement here compared to the previous one
print(squares)

#i**2 = The result you want to get
#for i in rnage(10) = the list or iterable that it is coming from
 #optional you can add a condition
 #e.g.
squares1 = [i for i in range(22,34) if (i%2) == 0]
print("squares1 are: ", squares1)
#if (i%2) ==0 = is the condition #(it is not a must you put the bracket)
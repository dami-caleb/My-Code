#sorting 2D list

data = [[2,3,4],[5,67],[87]]  #The iteration starts with the number that is lowest, is there
                              #is a conflict. e.g Two inner list start with the same number 
                              #it will check the second number and pick the list whoes second 
                              #number is the lowest
print(sorted(data))


#The same can be done with strings
stuff =[["Joy","Peace","Grace"],["Happy","Quite"],["Amazon"]]  #it is going to loo at the single elemnts in the list
                                                                #and put it first                                                                #it first looks at the first element of each list
                                                                #if the elements are the same it looks at the second
                                                                #element of the list
print(sorted(stuff))
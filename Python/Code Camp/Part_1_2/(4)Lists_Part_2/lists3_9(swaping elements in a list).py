#how to swap two variables

data = ["a","b","c"]

me = "Caleb"
you ="Friend"

#to swap this

me,you = you,me
print(me,you)

###############################
#Another way to swap, by using a temporary variable
#in other programming langusges this is actually the way it is done
me = "Caleb"
you ="Friend"

temp = me
me = you
you = temp 

print(me,you)



############################
#swaping elements in a list
data = ["a","b","c","d","e","f","g"]

index = 1

data[index], data[-index-1] = data[-index-1], data[index]
print(data[index],data[-index-1])

print(data)






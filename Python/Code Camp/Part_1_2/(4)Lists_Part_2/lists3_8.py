#How to reverse a list
data = [1,3,4,5,]
#we use the method ".reverse"

data.reverse()
#when you have a method that does not return anything (".reverse") you cant use it with a "print()"
# you have to type:

print(data)
#not: print(data.reverse())
#because nothing will be printed out🤔


##################################
#What we just did reverse the list
#if we want to revese a list but keep the original
copy_of_data = data[:]
copy_of_data.reverse()
print(copy_of_data)
print(data)
#now as you can see the copy is reversed and the original is kept











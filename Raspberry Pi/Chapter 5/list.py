
a = [23,32,45,23,True,"Hallo","Sup",23.45]
a[2] = True
print(a)

print("The length of the list a is",len(a)) #the return value of a is with a space


#You need to add an item to a list.
#Use the append, insert, or extend Python functions.

#To add a single item to the end of a list, 
#use append, as shown here:

a.append("Like")
print(a)

#To add items at a particular position in the list
#use insert
a.insert(3,"Yes") #remember list start counting from 0
print(a)

#Both append and insert add only one element to a list.
#The "extend" function adds all the elements of one list to the end of another

a = [34,42,'Friend']
b =[34, 45]

a.extend(b)
print(a)

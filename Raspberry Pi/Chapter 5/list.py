

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

#You need to convert a string of words separated by some character 
#into an array of strings, with each string in the array being one of the words.
#Use the split Python string function.
#The command split with no parameters separates out the words of a string into individual 
#elements of an array:

string = "Hello how are you?"
new_list = string.split()

#if you provide split with a parameter, it will split the string, using the parameter as a
#separator

string1 = "hello,gutten.tag"
print(string1.split(","))

#Iterating over a string
stuffs  = [3,2,4,"Joy"]

print("There are",len(stuffs)," items in the list stuff ")

for i in range(len(stuffs)):
	print("Item number ",i,"is ",stuffs[i-1])

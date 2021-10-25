#length_of_string

message = "Jesus is LORD"
number_of_characters = len(message) # The function "len" gets the number of charcters in a string (The length of a string)

print(len(message))


###########################
# Note that the index is not
#the same as the length.
#The index starts at 0
#The length starts at 1
#So therefore the index is always
#going to be one number less than
#the length.
#Why?
#In normal everyday counting, when we count, we start counting from 1, so therefore in the same way if we want to get the number of characters we start counting from 1
#
#The index on the other hand starts counting from 0. Remeber we use the index to get a charcter, or set of characters from a string
#############################

print(number_of_characters) #This gives the number of characters in every day human language

print(message[3])#index: gets a charcter
print(message[0:5])#index: gets a set of characters from a string
print(message[0:-8])

######################################
word = "GOD IS LOVE"
length_substraction = word[len(word) - 1] #This grabs the last character. The same as print(word[10])
print(length_substraction)
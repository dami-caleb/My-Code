#String slicing
#we can use slicing to grab a set of characters in a string

question= "How old are you"

print(question[2:])# Does not include the first two letters (excludes the first two letters) 
#prints from index 3 to the end (starts printing from the 3rd letter)

print(question[:2])# Does not include anything after the first two letters(includes the first two letters only) 
#prints from index 0-1 (stops at index 1)

print(question[8:11])

print(question[:-4]) # - starts from the back

print(question[:-4] + " How are you")

print(question[8:-4])

begin= 8

print(question[begin:begin-12])

print(question[35:54]) #if it is not a valid range it is still going to work in slicing

#question[start_at : stop_at]
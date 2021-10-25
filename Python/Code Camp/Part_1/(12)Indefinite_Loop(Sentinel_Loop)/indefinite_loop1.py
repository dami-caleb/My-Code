""" 
while True:
    print("Continue? Y/N")
    response =input()
    if response =='Y' or response =="y":
        continue
    break
"""

#################
#To prevent the secanrio of writing both uper and lower case letters
#we can use the ".lower" method. 
#What this does is, it converts any alphabet(character) entered to lower case
#Example:

while True:
    print("Continue? Y/N")
    response =input()
    if response.lower() !='y':
        break

#################
#There is also the ".upper" method:
#that converts to uppercase

name = input("What is your name: ")
print(name.upper())
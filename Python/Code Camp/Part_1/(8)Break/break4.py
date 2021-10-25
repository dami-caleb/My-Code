#else part 2 = else with a loop (for, while)
languages = ["C", "C++","Java", "Python", "Java Script", "Swift", "SQL","Rugby"]

print("Which programming language, do you want to use today?")
user_choice = input()

for language in languages:   #Remember what this does is to go through each element in the list
    if language == user_choice:
        print("We found " + user_choice)
        break
else:
    print("loop is done")


""" 
#Another of doing this is with a flag variable
#this is pretty much a bolean that tells you to do something later on in your code.
found = False

for language in languages:   #Remember what this does is to go through each element in the list
    if language == user_choice:
        print("We found " + user_choice)
        found = True
if not found:
    print("We don't have that programming language")
"""
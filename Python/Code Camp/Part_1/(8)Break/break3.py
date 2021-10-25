#pass
#The key word "pass" is a way of developers to say I will come back and put something there later
# the key word "pass" is used as a place hoöder till you have a better solution to the problem 
# pass is another way of saying I will come back later to that part

languages = ["C", "C++","Java", "Python", "Java Script", "Python", "Java","C++"]
pass
print("Which programming language, do you want to use today?")
pass
user_choice = input()
pass
for language in languages:   #Remember what this does is to go through each element in the list
    pass
    if language == user_choice:
        pass
        print("We found " + user_choice)
pass

#the pass does not affect your code in any way
# anytime you are writing a line of code and something is needed but you don't
#know what to put there, you can type pass
#e.g
for language in languages:  
    pass                         #obviously something is needed here. If you dont't know what to put at the moment, writing "pass" will make it possible for you to leave it blank and without affecting the code
    

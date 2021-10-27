#"continue"
# continue = instead of quiting the entire loop, it leaves the loop it is curently working in, and goes to the next one

languages = ["C", "C++","Java", "Python", "Java Script", "Python", "Java","C++"]
"""
print("Which programming language, do you want to use today?")
user_choice = input()

for language in languages:   #Remember what this does is to go through each element in the list
    if language == user_choice:
        print("We found " + user_choice)
        continue
    print(language + "...Not we are looking for..")
"""


number_of_times_found = 0

print("Which programming language, do you want o use today?")
user_choice = input()

for language in languages:   #Remember what this does is to go through each element in the list
    if language == user_choice:
        print("We found " + user_choice)
        number_of_times_found += 1
        continue
    print(language + "...Not we are looking for..")

print("We found " + user_choice + " " + str(number_of_times_found) + " times.")

#Note
#This does not work with nested lists




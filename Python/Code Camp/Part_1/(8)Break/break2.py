#another variation of continue is "else"

languages = ["C", "C++","Java", "Python", "Java Script", "Python", "Java","C++"]

print("Which programming language, do you want to use today?")
user_choice = input()

for language in languages:   #Remember what this does is to go through each element in the list
    if language == user_choice:
        print("We found " + user_choice)
    else:
        print(language + "...Not we are looking for..")

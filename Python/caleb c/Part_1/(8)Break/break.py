#Breaking out of a loop

languages = ["C", "C++","Java", "Python", "Java Script", "Swift", "SQL","Rugby"]
""" 
print("Which programming language, do you want o use today?")
user_choice = input()

for language in languages:   #Remember what this does is to go through each element in the list
    print (language)
    if language == user_choice:
        print("We found " + user_choice)
        break
    print("End of loop iteration")
"""



print("Which language are you loooking for?")
user_answer = input()

for i in range(len(languages)):
    print(i,languages[i])
    if languages[i] == user_answer:
        print(languages[i] + " found")
        break
    print("Gone through element " + str(i+1) + " in the list.")


#break = The loop is done, it does not continue the loop, any more
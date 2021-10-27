#How to remove numerous items from a list

healthy =["almonds","nuts","lentils","oatmeal","wheat","broccoli","apple","kale","blueberries","avocados","vegetables","potatoes","fish","chicken","eggs"]      #https://www.medicalnewstoday.com/articles/245259#Fish,-meat,-and-eggs
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]
id(backpack)

backpack = [item for item in backpack if item in healthy]
id(backpack)  #The memory location has changed. This means another object (list) with the same name was created in memory (A new list with the same name was created)

print(backpack)



#########################
#one problem here is the location in memory of the "first backpack" is different from the "second backpack". That means two different object in memory were created
#To prevent the problem check the next file "lists2_5.py"
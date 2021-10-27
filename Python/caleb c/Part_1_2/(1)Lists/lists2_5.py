# To prevent the problem of lists2_4.py what we do is:
#we add [:] to the name of the lists. 

healthy =["almonds","nuts","lentils","oatmeal","wheat","broccoli","apple","kale","blueberries","avocados","vegetables","potatoes","fish","chicken","eggs"]      #https://www.medicalnewstoday.com/articles/245259#Fish,-meat,-and-eggs
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]
id(backpack)

backpack[:] = [item for item in backpack if item in healthy]
id(backpack)  #The memory location has not changed. This means another object (list)  was not created in memory (The same list "backpack" is what was updated)

print(backpack)
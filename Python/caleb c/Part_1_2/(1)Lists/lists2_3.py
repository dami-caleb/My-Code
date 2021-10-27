#How to remove elements from a list

healthy =["almonds","nuts","lentils","oatmeal","wheat","broccoli","apple","kale","blueberries","avocados","vegetables","potatoes","fish","chicken","eggs"]      #https://www.medicalnewstoday.com/articles/245259#Fish,-meat,-and-eggs
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

if "kale chips" not in healthy:
    backpack.remove("kale chips")

print(backpack)
#Lists comprehension syntax
#What we are going to do is to explain "item for item in backpack if item in healthy" in another way


healthy =["almonds","nuts","lentils","oatmeal","wheat","broccoli","apple","kale","blueberries","avocados","vegetables","potatoes","fish","chicken","eggs"]      #https://www.medicalnewstoday.com/articles/245259#Fish,-meat,-and-eggs
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips","wheat"]


backpack[:] = [item for item in backpack if item in healthy]
print(backpack)
print(id(backpack))

############################################## 
#let's explain it by doing it another way

healthy_backpack = []

for item in backpack:             #for each item in "backpack"
    if item in healthy:           #if the item is in healthy
        healthy_backpack.append(item)    #put it in healthy_backpack

print(healthy_backpack)

######################################################################
#for item in backpack:             
#    if item in healthy:           
#        backpack[:].append(item)    
#print(id(backpack))



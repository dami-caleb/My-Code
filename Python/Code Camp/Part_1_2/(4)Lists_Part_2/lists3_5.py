backpack = ["pizza slice","button","pizza slice", "fishing pole", 
"pizza slice", "snadwhich"]

print(backpack[2:4])  
#this is saying start at 2nd element in the list and stop at 4th(the 4th element is exclusive)

print(backpack[:])
#what this is saying is start at the begining of the list and stop at the end of the list
#this is why this is an efficent way pf copying a lists

second_backpack = backpack[:]  #This is a copy ()

#backpack and second_backpack are seprate objectes in memory it's just that they have the same content
print(id(backpack))
print(id(second_backpack))
#Two diffrent objects

#############################
#we can also use [:] to change the entire content of a list
backpack[:] = [2,4,5]
print(backpack)
print(id(backpack))
#you notice this has the same id(location in memory) as the original backpack.
#by "doing backpack[:] =" and asigning it elements, we changed everything in the list backpack. We did not create a copy, but changed everything
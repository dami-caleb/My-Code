#Copying lists part 2

import copy

stuff = ["Learn", 12, "Fun", ['CODE','PROGRAMING', 'GOING TO THE GYM']]
the_counterfit = copy.deepcopy(stuff)#Now this is the best way to "copy a list" and "not affect the original".

print(stuff, the_counterfit)

###################################
#The "copy.deepcopy()" function also works for normal strings
name = "Mike"
other_name = copy.deepcopy(name)
print(other_name)





 
 



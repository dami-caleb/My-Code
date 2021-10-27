#Nested lists

#A nested lists is when you have a list in a list
#e.g.
stuff = ["Learn", 12, "Fun", ['CODE','PROGRAMING', 'GOING TO THE GYM']] #two dimentional nested list

#print(stuff[3])

#print(stuff[3][0])
#print(stuff[3][1])
#print(stuff[3][2])


stuff1 = stuff = ["Learn", 12, "Fun", ['CODE',"Football",['PROGRAMING', 'GOING TO THE GYM']]]
#                   0       1    2    3  "0"     "1"    "2"    #0            #1                
print(stuff[0])
#print(stuff1[3])
#print(stuff1[3][0])
#print(stuff1[3][1])
#print(stuff1[3][2])
print(stuff1[3][2][0])
print(stuff1[3][2][1])

print(len(stuff1[3][2]))









##########################################################################################
#The shallow copy (".copy") does not work for inner lists
#The shallow copy: Changing something in the inner list of a list in a shallow copy will affect the original
#shallow copy ".copy" only works for one dimentional lists

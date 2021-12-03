#2D lists

grades = [[23,45,67,89],[200],[12,33,77,90]]

print(grades[2][3]) 

grades[1].append(80) #we can append by by adding the list number 
print(grades)

for iner_list in grades:
    iner_list.append(90) #we add 90 to every list
    for grade in iner_list:
        print(grade,end=" ") #The ' end="" ' prints a newline
    print()   #this breaks it out by list
    
for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j], end=" ")
    print()
    

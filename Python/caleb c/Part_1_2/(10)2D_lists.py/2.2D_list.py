#2D lists

grades = [[23,45,67,89],[200],[12,33,77,90]]




def TwoD_list_printer(number):
    for iner_list in grades:
        for grade in iner_list:
            print(grade,end=" ") #The ' end="" ' prints a newline
        print()   #this breaks it out by list
    

TwoD_list_printer(grades)    #The definition of the function has to come beforethe

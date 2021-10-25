def print_info(name,age,email):
    print(name, "is", str(age), "and can be reached at", email )

info = ["Caleb",12,"caleb@email.com"]

print_info(*info) #The "*" in front of the list (get_info) opens the list 

#######################
#you can do it the old way
print_info(info[0],info[1],info[2])

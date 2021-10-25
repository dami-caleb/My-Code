#We can count the number of times something is repeated in a lists
#.count

backpack = ["sword","rubber duck","slice of pizza","parachute","sword","sword"]
number_of_times_repeated = backpack.count("sword")
print("The word sword is repaeated: "+ str(number_of_times_repeated) + " times in the list")

if backpack.count("sword") <4:
    backpack.append("sword")




###############################
#while backpack.count("sword") != 1:
#    backpack.remove("sword")

#print(backpack)
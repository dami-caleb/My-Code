
print("Welcome to the times table")
print("This multiplication table shows you the times table up to 13")

for i in range(14):
    print(i, "times table:")
    for j in range (13):
        result = i*j
        print(str(i)+ "*" + str(j) + " =" + str(result) )

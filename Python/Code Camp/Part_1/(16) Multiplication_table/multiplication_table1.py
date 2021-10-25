print("Welcome to the multiplication table provider :)")

multiplication_table = int(input("Kindly enter the multiplication table you would like to see: "))
end_of_table = int(input("Where will you like to end the multiplication table: "))

i = 0

while i<= end_of_table:
    result = multiplication_table*i
    print(str(multiplication_table)+ "*" +str(i) + " = " + str(result))
    i +=1
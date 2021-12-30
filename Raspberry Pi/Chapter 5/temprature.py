

def Celsius_to_Fahrenheit():
    tempC = int(input("Enter the Celsius temprature you want to conver to Fahrenheit: "))
    tempF = ((tempC)*9)/5 +32
    print("The temprature in Fahrenheit is ", tempF)

#Celsius_to_Fahrenheit()

def Binary_to_Decimal():
    binary_value = input("Enter the binary value you wish to convert to decimal: ")
    decimal_value = int(binary_value,2)
    print("The decimal equivalent of ", binary_value, "is ", decimal_value)

#Binary_to_Decimal()

def Hex_to_Dec():
    hex_value = input("Enter the hexadecimal value you wish to convert to decimal: ")
    decimal_value = int(hex_value,16)
    print("The decimal equivalent of ", hex_value, "is ", decimal_value)


#You need to find the position of one string within another.
#Use the find Python function.

#For example, to find the starting 
# position of the string "wwe" within 
# the string frfwwevvvv, you would use:

s = "frfwwevvvv"
print(s.find("wwe"))

#You want to replace all occurrences of a string within another string.
#Use the replace function.
#For example, to replace all occurrences of X with times, 
# you would use the following:
s = "It was the best of X. It was the worst of X"
print(s.replace("X", "times"))
print(s)




#print(f"""crrf/|+
#\gf%""")
#formating numbers
x= 1.987654321
print("x={:.2f}".format(x)) #The result returned by the format method is a string
#In the preceding example, the format specifier is :.2f, which
#means that the number will be specified with two digits after the
#decimal place and is a float f.

print("If you wanted the number to be formatted so that the total length of the number is always seven digits (or padding spaces): ", "x={:07.02f}".format(x) )

c = 20.5
print("Temperature {:5.2f} deg C, {:5.2f} deg F.".format(c,c*9/5 +32))

#using the format method to display numbers in binary
print("binary foramt of 42 is {:b}".format(42))

print("Hexadecimal format of 42 is {:X}".format(42))

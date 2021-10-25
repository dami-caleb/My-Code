#lists comparison
#we can also compare lists

ages_in_class_1 = [4, 5, 3]
ages_in_class_2 = [1, 3, 5]

print("Are the ages in both classes the same? "+ str(ages_in_class_1 == ages_in_class_2))
print("Are the ages in both classes the same? ", ages_in_class_1 == ages_in_class_2)

ages_in_class_1 = [1, 2, 3]
ages_in_class_2 = [1, 2, 3]
print ("are the ages the same object now they have the same values? ",ages_in_class_1 is ages_in_class_2 )

ages_in_class_1 = ages_in_class_2
print("are ages the same obeject now that they are pointing to the same object in memeory? "+ str(ages_in_class_1 is ages_in_class_2))

print("is ABC < BCD", "ABC"<"BCD")
print("is ABC < BCD " + str("ABC"<"BCD"))

print("A!=B", "A"!="B")

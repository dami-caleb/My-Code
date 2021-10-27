#We are going to sort the data in the list "stuff" as if they numbers(intgers)
#althogh they contain differnt data types

age =4
stuff = [True, False, 0, -1, "0","1","10",age <10,"20","2","5","9001","5.5","6.0",5]

stuff.sort(key=float)
print(stuff)

#age<10 is True that is why you see an extra "True"s in the output.
#Remember True=1, False =0

#Notice
#none of the data is a string that can not be converted (i.e. all the data
# in the list must be convertable)
 




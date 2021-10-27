msg = "Hey Pizza"
print(msg)

#escape charcters:
#\n new line
#\t tab (big space)
# "\"" to print a double quote
#"\\t" to print \t

#in python double quotes and single quotes work the 
#same way

msg1 = "You're great" #if you want to put single quotes in your sting use double quotes
msg2 = 'Damilola: "I know"'# if you wnat to use double quotes n your string use single quotes

#There are escape characters as disscused above that let you use double quotes in- 
#a double quote string, and single quote in a single quote string
# example: "She said \"Hi\"" The same thing works with single quote (backslash makes it possible)

###################################################
#Note:
#To print out special characters such as: '"\ etc.
#we use backslash -->\

###################################################
#You can also prefix with r which will make a raw string (makes it posssible to print out escape characters without a problem)
#
#print(r 'the r infront makes it possbile to type(print) special/escape  charcters: \/ () \/. \t without having to type the backslash (except the quote --> ’ or " that ends the print statement. So to print the quote used to start the print statement you need the backslash ')
#

print(r"GOD says \" Your awsome\" Damilola \/ () \/. \t ")
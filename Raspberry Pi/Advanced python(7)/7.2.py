#Formating dates and time:
#In this file we will convert a date into a string and format it in a certain way.

#We do this by applying a "format" string to the date object
from datetime import datetime
curreent_date = datetime.now()
print("{:%Y-%m-%d %H:%M:%S}".format(curreent_date))

#The Python formatting language includes some special symbols for
#formatting the date. %y (which gives the year without century as a
#zero-padded decimal number), %m, and %d correspond to year,
#month, and day numbers, respectively
updated_date = datetime.now()
print("Today's year, month, and date respectively is: {:%Y, %B, %d}".format(updated_date))

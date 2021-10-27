#How to remove elements from a list "anywhere"

days_of_the_week = ["Monday","Wednesday","Friday","Saturday"]

days_of_the_week.remove("Friday") #you have to know the name of the element
print(days_of_the_week)

################################
#Another alternative (if you don't know what the data is, but you know the location of the data). If you don't know the name of the element, but you know the position (index) of the element you want to remove

del days_of_the_week[2]
print(days_of_the_week)
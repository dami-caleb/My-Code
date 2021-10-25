#How to remove slices from a list

days_of_the_week = ["Monday","Wednesday","Friday","Saturday"]

#del days_of_the_week[-1]
#this takes away the last element

del days_of_the_week[1:3]
print(days_of_the_week )


#############################
#another way of typing: del days_of_the_week[1:3]
days_of_the_week = ["Monday","Wednesday","Friday","Saturday"]
del days_of_the_week[days_of_the_week.index("Wednesday"):days_of_the_week.index("Wednesday") +2]
print(days_of_the_week)
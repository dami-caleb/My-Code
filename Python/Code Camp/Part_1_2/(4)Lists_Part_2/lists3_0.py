#Here we will be talking about how to add elements to a list anywhere we want

days_of_the_week = ["Monday","Wednesday","Friday","Saturday"]

days_of_the_week.insert(1,"Tuesday")  #The first argument "1" is the location where you want to insert the element (The index). And the second argument "Tuesday", is what you actually want to insert to the list
print(days_of_the_week)

days_of_the_week.insert(3,"Thursday") #Notice how the index increased by 1. This is because we have added an element to the list previouly so the number of the elements in list has increased. It is always good to check.
print(days_of_the_week)


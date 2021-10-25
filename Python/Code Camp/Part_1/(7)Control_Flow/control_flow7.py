#for loop vraition 2

foods = ["Rice", "Beans","Chicken","Potatoes","Fries","Turkey"]

for i in range(len(foods)):  #instead of passing a number (10) we are passing the length of food
    print(i, foods[i], end=" ")
print() 
#what this does is it prints the elements in the foods list, with numbers
#it's kind of a combination of the first two example above

#lET'S BREAK DOWN THE CODE ABOVE
number = len(foods)
print("The length is " + str(number))


for i in range (number):
    print(i, end=" ")
print()

for i in range (number):
    print(foods[i], end=" ")
print()

####################################

#Let's combine the code
for i in range (len(foods)):
    print(i,foods[i])
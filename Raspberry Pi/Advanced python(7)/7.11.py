#Using modules

#Modules are somethimes called library
import random as R

my_list  = ['a','r','t',1,3,5]

print(R.choice(my_list))

#another way
random_number = R.randint(0,6)
print("The random item is " + my_list[random_number])

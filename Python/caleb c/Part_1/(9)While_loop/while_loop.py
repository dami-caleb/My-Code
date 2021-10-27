#The while loop is based on three mottos (I.C.U)
#initialization
#condition
#update

i = 0  #initialization

while i< 10: #condition
    print("Yellow!...",end = " ")
    i += 1 #update
print()

#Classwork
#(1) Modify the loop to count in 5's up to 15
#(2) Modify the loop to count backwards

#Solution


#(1)
print("Number 1 solution:")
number = 0

while number < 15:
    print(number)
    number += 5
print()

#(2)
print("Number 2 solution:")
constant = 10

while constant >=0:
    print(constant)
    constant -= 1 



#The While loop actually works the same way as the for loop
#####################
#e.g.
#for i in range(initilization(start at),condition(stop at),update(increase by)):
#   print(i)
#
#######################
#Actual Example
for i in range(2,22,4):
    print(i, end=" ")
print()
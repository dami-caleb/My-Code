#now concerning our previous example in (7)loop.py
#we want to be able to remove fruits as well

print("What are your favourite fruits? Press enter after each fruit")
print("Enter 'r' to remove and 'q' to quit: ")

fruits = []

while True:
    data = input()
    if str.lower(data) =='q':
        break
    elif str.lower(data) == 'r':
        print("Removing latest input \""+fruits.pop() + "\"")
        print("Data removed. Enter next fruit or enter 'q' to quit")
    else:
        fruits.append(data)
    
    
for fruit in fruits:
    print("one of your favourite fruit is: ",fruit)
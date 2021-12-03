#hOW TO USE A LIST HAS A QUEE

######################################################
queue = []

queue.append("Data1")
queue.append("Data 2")

queue.pop(0) #the queue removes the items with the lowest index
print(queue)
######################################################

#The queue is first in first out

print("What are your favourite fruits? Press enter after each fruit")
print("Enter 'r' to remove and 'q' to quit: ")

fruits = []

while True:
    data = input()
    if str.lower(data) =='q':
        break
    elif str.lower(data) == 'r':
        print("Removing latest input \""+fruits.pop(0) + "\"")
        print("Data removed. Enter next fruit or enter 'q' to quit")
    else:
        fruits.append(data)
    
    
for fruit in fruits:
    print("one of your favourite fruit is: ",fruit)



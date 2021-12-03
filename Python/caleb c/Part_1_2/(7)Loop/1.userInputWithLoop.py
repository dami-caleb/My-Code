print("What are your favourite fruits? Press enter after each fruit")
print("Enter 'q' to quit: ")

fruits = []

while True:
    data = input()
    fruits.append(data)
    if str.lower(data) =='q':
        break
    
    
for fruit in fruits:
    print("one of your favourite fruit is: ",fruit)
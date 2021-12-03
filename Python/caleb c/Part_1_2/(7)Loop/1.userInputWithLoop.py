print("What are your favourite fruits?")
print("Enter 'q' to quit: ")

fruits = []

while True:
    data = input()
    if str.lower(data) =='q':
        break
    fruits.append(data)
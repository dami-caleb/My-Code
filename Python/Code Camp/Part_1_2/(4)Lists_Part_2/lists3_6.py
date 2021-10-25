#How to remove all instances of an element in a list using the for loop
bagpack = ["pizza slice","button","pizza slice", "fishing pole", 
"pizza slice", "snadwhich"]


for item in bagpack:
    if item =="pizza slice":
        bagpack.remove(item)

print(bagpack)
#As good programmers you never remove items froma list with the for loop
#it shifts the indexes



#Solution#:
#to prevent the shift of indexes and solve the problem
for item in bagpack[:]:
    if bagpack.count(item) > 1:
        bagpack.remove(item)















""" 
i = 0

while bagpack.count(bagpack[i]) >1:
    bagpack.remove(bagpack[i])
    i += 1
"""







backpack = ["pizza slice","button","pizza slice", "fishing pole", 
"pizza slice", "snadwhich"]

new_backpack = []

for item in backpack:
    if item != "pizza slice":
        new_backpack.append(item)

backpack = new_backpack
print(backpack)
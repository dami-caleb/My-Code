#How to remove an repeated elements in a list

backpack = ["pizza slice","button","pizza slice", "fishing pole", 
"pizza slice", "snadwhich"]

while backpack.count("pizza slice") > 1:
    backpack.remove("pizza slice")

print(backpack)


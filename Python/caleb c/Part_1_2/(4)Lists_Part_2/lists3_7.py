#Al to remove all instances of an item in a list
#using lists comprehension

bagpack = ["pizza slice","button","pizza slice", "fishing pole", 
"pizza slice", "snadwhich"]

bagpack[:] = [item for item in bagpack if item != "pizza slices" ]

print(bagpack)


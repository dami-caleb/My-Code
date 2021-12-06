#how to remove duplicates from a list
foods = ["Rice","Rice","Rice","Fish","Fish","Beans"]

#to use the same object in memory
foods[:] = list(set(foods))
print(foods)
foods = ["Rice","Rice","Rice","Fish","Fish","Beans"]

counter =[[foods.count(food), food] for food in set(foods)]

print(counter)
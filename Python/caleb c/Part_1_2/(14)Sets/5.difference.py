my_fav = {"red","green","blue","black","purple"}
her_fav = {"blue", "orange","purple","green"}

#Difference(A-B) or (B-A):
only_me =  my_fav - her_fav
only_her = her_fav -my_fav
print(only_me) #the elements that are not in her_fav but in my_fav is what is printed out

print(only_her) #the elements that are not in my_fav but in her_fav is what is printed out


#Symetric Difference((A-B) | (B-A)):
sym_diff = only_me | only_her
print(sym_diff)

#There is an operator to do this.
Symetric = my_fav ^her_fav
print(Symetric)



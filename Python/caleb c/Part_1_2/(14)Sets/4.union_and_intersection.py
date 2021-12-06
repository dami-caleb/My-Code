my_fav = {"red","green","blue","black","purple"}
her_fav = {"blue", "orange","purple","green"}

all_favs = my_fav | her_fav #union 
print("The unioun of set 'my_fav' and 'her_fav' is ",all_favs) #no repetead data

#in al list the + sign is okay (i.e a concatenation)

common_colours = my_fav & her_fav #the & is used for intersection 
print("The intersection of my_fav and her_fav is ",common_colours)

#The intersection of two or more given sets is the set of elements that are common to each of the given sets. 
#remeber from secondary school mathematics.

#another way of doing intersection and union is
common_colours = my_fav.intersection(her_fav)
all_favs = my_fav.union(her_fav)
#How to sort a list by length

random = ["a","A","aa","AAA","HELLO","b","c","d"]

random.sort(key=len)
print(random )

########################################################
#another way to do it is to use the "sorted(function)"
random = ["a","A","aa","AAA","HELLO","b","c","d"]
new_random = sorted(random, key=len)

#using this function the original list is not changed, compared
#to using the ".sort()" method.
###########################################################
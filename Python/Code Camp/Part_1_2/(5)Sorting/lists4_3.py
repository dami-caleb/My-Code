#When we sort a lis, it is case sensitive
#that is the upper case alpabets are given the highest priority
# let's see

alphabets = ["a","A","abc","ABC","aBc","aBC","Abc"]

#alphabets.sort()
#print(alphabets) #notice how the letetrs in Uppercase are put in front

#to make the ".sort" method not case sensitive
# we introduce a "key" as an argument for the method

alphabets.sort(key=str.lower) #notice we did not put an extra bracket after the .lower
print(alphabets)


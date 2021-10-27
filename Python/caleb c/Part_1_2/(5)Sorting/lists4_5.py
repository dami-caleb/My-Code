#How to sort numbers and compare them as they are strings
#(lexicographically)

data = [1,54,76,12,111,11,4343,6,8888,3,22,1,0,222,-1,-122,5,-30]

#so what is supposed to happen is the numbers in the list "data"
#will be sorted according to their "numeric oder" not size

data.sort(key=str)

print(data)
#notice the actual data in the list "data" 
#are still integers (numbers), they did not chage
#We did not convert the data in the list to a string


#We are going to first learn how to turn a string
#to a list

msg = "How are you today?"

words = msg.split() ###what this does is to sepreate the string
            ###by speaces and make them elements in the list
print(words)

#####################################
#you can also seprate by different elements

message = "Ho,w ar,e you,today?"
new_words = message.split(',')
print(new_words)
#We told python anywhere you see a comma split it
#notice that the spaces are not ignored



 #####################################
 #if you don't want the space to be printed out
quote = "Today, is, a, good, day!"
new_quote = message.split(', ') #we leave a space after the comma
print(new_quote)

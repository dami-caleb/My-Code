#Pickling

#If you want to save the entire contents
#of a data structure to a file so that it
#can be read the next time the program is
#run. Use: Python pickling

import pickle
mylist = ['some text', 123, [4,5,True]]
f = open('mylist.pickle','wb')
pickle.dump(mylist,f)
f.close()

#To unpickle the contents of the file
#(i.e use in memory/ or another source code)
#use:
f = open('mylist.pickle','rb')
james_list = pickle.load(f)
f.close()
print(james_list)

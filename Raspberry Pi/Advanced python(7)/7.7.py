#Writing a file
#Use the open, write, and close functions
# to open a file, write
#some data, and then close the file, respectively

f = open('test.txt','w')
f.write('This is a file')
f.close()
#ote that it is important to use close
#because, although each write should update
#the file immediately, it might be buffered in memory
# and data could be lost.



#Reading from a file
f = open('test.txt')
s = f.read()
f.close()
print(s)


#To throw an exception if a file does not exist
#or cannot be read use: "try"/"except"
try:
    f=open('test.txt')
    s = f.read()
    f.close()
except IOError:
    print("Cannot open the file")

##################################
#Practice
C_file = open('myfile.c','w')
C_file.write("#include <stdio.h>")
C_file.close()

image= open("my_image.png",'wb')
image.close()

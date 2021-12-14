"""
FILE HANDLIMG
#openning a file
fileobject=open("paht/to/file","mode")

'r'
"""
#open file
file=open("notes","r")
#read the file
print(file.read())#whole text
print(file.read(30))#read 30 char

print(file.readline())#read line

#loop throughtext line by line
for line in file:
    print(file)

#close file after u are done
#fileobject.close()
file.close()

#writting to a file
file=open("textfile.txt","w")
file.write("this is written in python"
           "lets check whether it works ")
file.close()


#writtin g to an existing mode

file=open("textfile.txt","a")
file.write("this is added content")
file.close()

import os
#os.remove("textfile.txt")
if os.path.exists("textfile.txt"):
    os.remove("textfile.txt")

else:
    print("file does not exist")
""" 
Write a Python program to write a list to a file.
"""

mylist=["banana","orange","apple","date"]

f=open("myfile.txt",'w')
for item in mylist:
    f.write(item + "\n")
f=open("myfile.txt",'r')
file=f.read()
print(file)
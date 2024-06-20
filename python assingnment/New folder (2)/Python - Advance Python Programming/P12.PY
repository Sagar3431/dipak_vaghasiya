""" 
Write a Python program to copy the contents of a file to another file.
"""
myfile="myfile.txt"
myfile1="myfile1.txt"

with open(myfile,"r") as file,open(myfile1,"w") as file1:
   contant= file.read()
   file1.write(contant)
print(f"contant copy from {myfile} to {myfile1}")
    
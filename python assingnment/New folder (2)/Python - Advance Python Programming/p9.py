""" 
Write a Python program to count the number of lines in a text file.
"""

f=open("myfile.txt",'r')
lines=f.readlines()
print(len(lines))

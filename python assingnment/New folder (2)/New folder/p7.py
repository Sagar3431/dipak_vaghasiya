""" 
Write a Python program to read a file line by line store it into a variable.
"""
f=open("myfile.txt",'r')
file_store=''# Initialize an empty string to store the content
for line in f:
    file_store+=line
    
print(file_store)
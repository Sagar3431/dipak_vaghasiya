""" 
Write a Python program to read a file line by line and store it into a list
"""
f=open("myfile.txt",'r')
list_store=[]#create empty list
for item in f:
    list_store.append(item.rstrip("\n"))#append and store into a list
    
print(list_store)
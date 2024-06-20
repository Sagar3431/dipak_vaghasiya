"""
Write a Python program to read last n lines of a file.
"""

f=open("myfile.txt",'r')
file=f.readlines()#readline is givan to fist line in text file
print(file[-1:])
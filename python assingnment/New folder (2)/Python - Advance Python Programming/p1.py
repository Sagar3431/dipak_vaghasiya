""" 
What is File function in python? What is keywords to create and write
file.

Python provides several built-in functions for file handling:

open(): Opens a file and returns a file object.
close(): Closes the file.
read(): Reads the contents of a file.
write(): Writes data to a file.
readline(): Reads a single line from a file.
readlines(): Reads all the lines from a file as a list.
"""
f=open("myfile.txt",'w') #create write file
f.write("hello python i am dipak vaghasiya")
f.close() #close file

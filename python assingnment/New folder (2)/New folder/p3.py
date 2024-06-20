""" 
Write a Python program to append text to a file and display the text.
"""

append_text="hello world"#str store in variable

f=open('myfile.txt','a')#create append
f.write(append_text)#write method and append str
f=open('myfile.txt','r')
file=f.read()#read file
print(file)#print file
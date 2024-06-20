""" 
Write a python program to find the longest words.
"""
f=open("myfile.txt",'r')
file=f.read()
words=file.split()#Split the content into words
longest_words=max(words,key=len)#Find the longest word
print(longest_words)
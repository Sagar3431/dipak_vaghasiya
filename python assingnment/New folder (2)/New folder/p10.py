""" 
Write a Python program to count the frequency of words in a file.
"""
from collections import Counter
import string
f=open("myfile.txt",'r')
text=f.read()
translator=str.maketrans('','',string.punctuation)
cleaned_text=text.translate(translator)
clean=cleaned_text.lower()
words=clean.split()
word_count=Counter(words)
for word,frequency in word_count.items():
    print(f'{word} : {frequency}')
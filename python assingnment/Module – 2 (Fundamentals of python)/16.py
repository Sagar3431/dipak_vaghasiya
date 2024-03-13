'''
Write a Python program to count the occurrences of each word in a given sentence
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word occurrences:")
for word, count in word_freq.items():
    print(word, ":", count)

            



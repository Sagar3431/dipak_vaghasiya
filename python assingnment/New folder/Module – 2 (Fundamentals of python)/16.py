'''
Write a Python program to count the occurrences of each word in a given sentence
'''
# Prompt the user to enter a sentence and store it in the variable sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words and store them in a list called words
words = sentence.split()

# Create an empty dictionary to store word frequencies
word_freq = {}

# Iterate through each word in the list of words
for word in words:
    # Check if the word is already in the word_freq dictionary
    if word in word_freq:
        # If the word is already in the dictionary, increment its count
        word_freq[word] += 1
    else:
        # If the word is not in the dictionary, add it with a count of 1
        word_freq[word] = 1

# Print the word occurrences
print("Word occurrences:")
for word, count in word_freq.items():
    print(word, ":", count)


            



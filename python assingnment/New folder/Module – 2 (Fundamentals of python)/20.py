'''
Write a Python function that takes a list of words and returns the length
of the longest one.
'''

# Define a list of words
word_list = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

# Initialize a variable to store the maximum length found so far
max_length = 0  

# Iterate through each word in the word_list
for word in word_list:
    # Check if the length of the current word is greater than the maximum length found so far
    if len(word) > max_length:
        # If the current word is longer, update the maximum length
        max_length = len(word)

# Print the length of the longest word
print("Length of the longest word:", max_length)


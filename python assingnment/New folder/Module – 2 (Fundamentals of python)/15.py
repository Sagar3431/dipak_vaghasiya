'''
Write a Python program to count occurrences of a substring in a string.
'''

# Prompt the user to enter the main string and store it in the variable main_str
main_str = input("Enter the main string: ")

# Prompt the user to enter the substring to count and store it in the variable sub_str
sub_str = input("Enter the substring to count: ")

# Initialize a counter variable to store the count of occurrences of the substring
count = 0

# Initialize the start index for searching the substring within the main string
start_index = 0

# Start an infinite loop
while True:
    # Find the index of the next occurrence of the substring in the main string,
    # starting the search from the start_index
    index = main_str.find(sub_str, start_index)
    
    # If no more occurrences are found, exit the loop
    if index == -1:
        break
    
    # Increment the counter for each occurrence found
    count += 1
    
    # Update the start_index for the next search to be one character after the found occurrence
    start_index = index + 1

# Print the number of occurrences of the substring in the main string
print("Number of occurrences of '{}' in '{}' is: {}".format(sub_str, main_str, count))




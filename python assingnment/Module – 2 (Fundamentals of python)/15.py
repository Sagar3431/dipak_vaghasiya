'''
Write a Python program to count occurrences of a substring in a string.
'''

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to count: ")

count = 0
start_index = 0

while True:
    index = main_str.find(sub_str, start_index)
    if index == -1:
        break
    count += 1
    start_index = index + 1

print("Number of occurrences of '{}' in '{}' is: {}".format(sub_str, main_str, count))



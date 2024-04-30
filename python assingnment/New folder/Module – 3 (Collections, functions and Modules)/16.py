'''
Write a Python program to check whether a list contains a sub list
'''

# Define the main list
main_list = [1, 2, 3, 4, 5, 6, 7]

# Define the sublists to check
sublist1 = [2, 3, 4]
sublist2 = [5, 6, 8]

# Iterate over the main list
for i in range(len(main_list) - len(sublist1) + 1):
    # Check if the sublist1 is found starting from index i
    if main_list[i:i + len(sublist1)] == sublist1:
        print("Sublist1 is present in the main list.")
        break
else:
    print("Sublist1 is not present in the main list.")

# Iterate over the main list
for i in range(len(main_list) - len(sublist2) + 1):
    # Check if the sublist2 is found starting from index i
    if main_list[i:i + len(sublist2)] == sublist2:
        print("Sublist2 is present in the main list.")
        break
else:
    print("Sublist2 is not present in the main list.")

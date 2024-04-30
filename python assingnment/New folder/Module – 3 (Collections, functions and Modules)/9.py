'''
Write a Python function that takes two lists and returns true if they have
at least one common member.
'''

# Two example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Flag to track if common member is found
common_member_found = False

# Iterate through elements in list1
for item in list1:
    # Check if the element is present in list2
    if item in list2:
        # If a common element is found, set flag to True and break the loop
        common_member_found = True
        break

# Check if common member was found and print the result
if common_member_found:
    print("The lists have at least one common member")
else:
    print("The lists do not have any common members")

'''
Write a Python program to unzip a list of tuples into individual lists.
'''
list_tuple=[(1,'a'),(2,'b'),(3,'c')]
# Unzip the list of tuples into individual lists
unzipped_list=list(zip(*list_tuple))
# Print the individual lists
for i, st in enumerate(unzipped_list,1):
    print(f"List {i}:",st)
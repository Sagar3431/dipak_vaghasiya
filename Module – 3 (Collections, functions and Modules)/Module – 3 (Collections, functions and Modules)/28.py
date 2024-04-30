'''
Write a Python program to remove an empty tuple(s) from a list of tuples.
'''

list_tuple=[(1,2,3),(),(4,5,6),()]
#remove empty tuple from list
filter_list=list(filter(None,list_tuple))
print(filter_list)
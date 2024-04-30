'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''

def get_unique_elements(input_list):
    # Convert the input list to a set to remove duplicates
    unique_set = set(input_list)
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list

# Example usage:
input_list = [1, 2, 2, 3, 3, 4, 4, 5]
unique_elements = get_unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", unique_elements)

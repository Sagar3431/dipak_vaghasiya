'''
Write a Python script to print a dictionary where the keys are numbers
between 1 and 15.
'''
my_dict={}#blank dict
#Populate the dictionary with keys from 1 to 15
for i in range(1,16):
    my_dict[i]=f"value_{i}"
# Print the dictionary
print("Dictionary with keys between 1 and 15:", my_dict)
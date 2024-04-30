'''
How Do You Traverse Through A Dictionary Object In Python?
'''
# 1 using for loop

my_dict = {'a': 1, 'b': 2, 'c': 3}
# Traverse through keys
for key in my_dict:
    print(key)
# Traverse through values
for value in my_dict.values():
    print(value)
    
# Traverse through key-value pairs
for key,value in my_dict.items():
    print(key,value)
    
# 2 Using a while loop (less common and not recommended for dictionaries)
keys=list(my_dict.keys())
value=list(my_dict.values()) 

i=0
while i<len(keys):
    print(keys[i],value[i])
    i+=1
# 3 Using dictionary methods (keys(), values(), items())
# Traverse through keys
for key in my_dict.keys():
    print(key)

# Traverse through values
for value in my_dict.values():
    print(value)

# Traverse through key-value pairs
for key, value in my_dict.items():
    print(key, value)
    
# 4 Using dictionary comprehensions (to perform operations on dictionary elements)
# Double each value
doubled_dict = {key: value * 4 for key, value in my_dict.items()}
print(doubled_dict)
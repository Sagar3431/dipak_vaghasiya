'''
Write a Python program to replace last value of tuples in a list.
'''

list_tuple=[(1,2,3),(4,5,6),(7,8,9)]
new_value=10

for i in range(len(list_tuple)):
    #convert tuple to a list
    temp_list=list(list_tuple[i])
    #replace the last value with the new value
    temp_list[-1]=new_value
    #Convert the list back to a tuple
    list_tuple[i]=tuple(temp_list)
    
print(list_tuple)
    
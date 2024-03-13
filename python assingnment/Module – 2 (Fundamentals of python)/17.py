'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
'''

# def swap_first_two_chars(str1, str2):
#     # Check if both strings have at least two characters
#     if len(str1) >= 2 and len(str2) >= 2:
#         # Swap first two characters of each string
#         swapped_str1 = str2[:2] + str1[2:]
#         swapped_str2 = str1[:2] + str2[2:]
        
#         # Concatenate the swapped strings with a space in between
#         result = swapped_str1 + ' ' + swapped_str2
#         return result
#     else:
#         return "Both strings should have at least two characters"

# # Example usage
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# result_string = swap_first_two_chars(string1, string2)
# print("Result:", result_string)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1)>=2 and len(string2)>=2:
    swapped_str1 = string2[:2] + string1[2:]
    swapped_str2 = string1[:2] + string2[2:]
    print(swapped_str1 + ' ' + swapped_str2)
else:
    print("Both strings should have at least two characters")




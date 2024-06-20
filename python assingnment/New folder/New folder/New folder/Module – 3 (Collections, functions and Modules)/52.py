'''
Write a Python function that checks whether a passed string is
palindrome or not
'''
# def is_palindrome(s):
   
#     # Remove non-alphanumeric characters and convert to lowercase
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     # Check if the string is equal to its reverse
#     return s == s[::-1]

# # Example usage:
# string = "A man, a plan, a canal, Panama"
# print(is_palindrome(string))  # Output will be True

name=input("name : ")
if name == name[::-1]:
    print("palindrome")
else:
    print("not")

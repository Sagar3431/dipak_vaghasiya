'''
Write a Python script to check if a given key already exists in a
dictionary.
'''
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key to check for existence
while True:
   key_to_check = input("Enter key (a,b,c) : ")

   if key_to_check in my_dict:
       print(f"The key '{key_to_check}' exists in the dictionary.")
   else:
       print(f"The key '{key_to_check}' does not exist in the dictionary.")
       
   choice=input("y/n :")
   if choice=="y":
       True
   else:
       print("mulakat badal abhar")
       break
    
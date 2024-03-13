'''
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

num1=int(input("Enter First Num : "))
num2=int(input("Enter second Num : "))

if num1 == num2 or abs(num1-num2) == 5 or num1 + num2 == 5:
    print("true")
else:
    print("false")
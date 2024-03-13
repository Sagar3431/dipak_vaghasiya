'''
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

num1=int(input("Enter First Num : "))
num2=int(input("Enter second Num : "))
num3=int(input("Enter third Num : "))

if num1==num2 or num2==num3 or num1==num3:
    print("two value are equal sum : ",0)
else:
    print("The sum of three integers is : ",num1+num2+num3)
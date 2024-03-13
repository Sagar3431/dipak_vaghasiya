'''
Write a Python program to get the Factorial number of given number.
'''
num=int(input("num : "))
fact=1

if num<0:
   print("factorial of 0 does not exist")
if num==0:
   print("factorial of 0 is",1)
if num>0:
   for i in range(1,num+1):
      fact=fact*i
      print("the factorial of the givan number is ",fact)   
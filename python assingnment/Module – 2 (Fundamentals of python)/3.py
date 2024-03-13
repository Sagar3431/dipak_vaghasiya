'''
Write a Python program to get the Fibonacci series of given range.
'''

a=0
b=1
num=int(input("num : "))
if num==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c)
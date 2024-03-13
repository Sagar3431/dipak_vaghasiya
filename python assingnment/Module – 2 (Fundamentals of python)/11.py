# def sum_of_positive_integers(n):
#     if n <= 0:
#         return "Please enter a positive integer."
#     else:
#         total = 0
#         for i in range(1, n + 1):
#             total += i
#         return total

# # Example usage:
# n = int(input("Enter a positive integer n: "))
# result = sum_of_positive_integers(n)
# print("The sum of the first", n, "positive integers is:", result)


'''
Write a python program to sum of the first n positive integers.
'''

num1=int(input("Enter Your Num : "))

if num1<=0:
    print("please enter a positive integer.")
else:
    total=0
    for i in range(1,num1+1):
        total+=i
    print("The sum of the first",num1,"positive integers is:",total)

     
    


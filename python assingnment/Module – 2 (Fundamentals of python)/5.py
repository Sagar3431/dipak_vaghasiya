'''
What is the purpose continue statement in python?
Ans:The continue statement in Python is used inside loops (such as for or while loops) to skip the rest of the current iteration and proceed to the next iteration of the loop.
'''

for i in range(1, 6):
    if i == 3:
        continue  # Skip iteration if i equals 3
    print(i)

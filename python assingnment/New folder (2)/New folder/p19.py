""" 
How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.
"""
#Basic try and except
try:
    
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError 
    print("You can't divide by zero!")
    
#Using try, except, and finally
try:
    result = 10 / 2
    print("Result is:", result)
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError 
    print("You can't divide by zero!")
finally:
    # Code that always runs
    print("Execution completed.")


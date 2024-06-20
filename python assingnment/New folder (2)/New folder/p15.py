
""" 
When will the else part of try-except-else be executed?
"""
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    # This block runs if no exceptions were raised in the try block
    print("Result is:", result)
finally:
    print("Execution of the try-except-else-finally block is complete.")

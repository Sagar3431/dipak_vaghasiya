""" 
Can one block of except statements handle multiple exception?
"""
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except (ValueError, ZeroDivisionError) as e:
# Handle ValueError and ZeroDivisionError
    print(f"An error occurred: {e}")
finally:
# This block always runs
    print("Execution of the try-except-finally block is complete.")

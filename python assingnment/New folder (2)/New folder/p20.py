""" 
Write python program that user to enter only odd numbers, else will
raise an exception.
"""
class NotOddNumberError(Exception):
    """Custom exception for non-odd numbers."""
    def __init__(self, number):
        self.number = number
        self.message = f"{number} is not an odd number."
        super().__init__(self.message)

# Main execution
try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        raise NotOddNumberError(number)
    print(f"Thank you for entering an odd number: {number}")
except ValueError:
    print("That's not a valid number. Please enter an integer.")
except NotOddNumberError as e:
    print(e)
finally:
    print("Execution completed.")

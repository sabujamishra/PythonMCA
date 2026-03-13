# Program to demonstrate user-defined exception in Python

class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number not allowed: {value}")

def check_positive_number(num):
    try:
        if num < 0:
            raise NegativeNumberError(num) 
        else:
            print(f"Valid number: {num}")
    except NegativeNumberError as e:
        print(f"Error: {e}")
    finally:
        print("Execution of check_positive_number function is complete.")

check_positive_number(10)   
check_positive_number(-5)   

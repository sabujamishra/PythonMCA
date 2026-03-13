# Program to demonstrate basic exception handling in Python

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide numbers only.")
    finally:
        print("Execution of divide_numbers function is complete.")

# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)   
divide_numbers(10, "a") 

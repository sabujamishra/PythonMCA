add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Division by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

operations = {'+': add, '-': sub, '*': mul, '/': div}

if op in operations:
    print("Result:", operations[op](a, b))
else:
    print("Invalid operator")

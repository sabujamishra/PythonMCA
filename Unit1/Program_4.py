# Program to find Armstrong numbers from 10 inputs

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def is_armstrong(num):
    digits = str(num)
    length = len(digits)
    total = 0
    for d in digits:
        total += power(int(d), length)
    return total == num

numbers = []
print("Enter 10 numbers:")
for i in range(10):
    n = int(input(f"Number {i+1}: "))
    numbers.append(n)

armstrong_numbers = [n for n in numbers if is_armstrong(n)]

print("Armstrong numbers are:", armstrong_numbers)

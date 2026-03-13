# Program to find the largest odd number among 10 inputs

numbers = []
print("Enter 10 numbers:")
for i in range(10):
    n = int(input(f"Number {i+1}: "))
    numbers.append(n)

odd_numbers = [num for num in numbers if num % 2 != 0]

if odd_numbers:
    largest_odd = max(odd_numbers)
    print("The largest odd number is:", largest_odd)
else:
    print("No odd numbers were entered.")

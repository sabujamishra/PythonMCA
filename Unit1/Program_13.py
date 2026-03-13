from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

total = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", total)

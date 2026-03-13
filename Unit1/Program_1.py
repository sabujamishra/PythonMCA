# Program to calculate Simple Interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
n = float(input("Enter the time in years: "))

interest = (p * r * n) / 100

print("The Simple Interest is:", interest)

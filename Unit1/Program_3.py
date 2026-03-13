# Program to calculate total, percentage and grade for 4 subjects

marks = []
print("Enter marks of 4 subjects:")
for i in range(4):
    m = float(input(f"Subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 4

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

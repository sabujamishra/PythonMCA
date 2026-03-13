def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "F"

def process_student_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Student Details:\n")
            for line in file:
                if not line.strip():
                    continue

                data = line.strip().split(',')

                roll_no = data[0]
                name = data[1]
                marks = list(map(int, data[2:]))
                
                total = sum(marks)
                percentage = total / (len(marks) * 100) * 100
                grade = calculate_grade(percentage)
                
                print(f"Roll No: {roll_no}")
                print(f"Name: {name}")
                print(f"Marks: {marks}")
                print(f"Total: {total}")
                print(f"Percentage: {percentage:.2f}%")
                print(f"Grade: {grade}")
                print("-" * 40)
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

filename = "students.txt"
process_student_file(filename)

students = []

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks (comma separated): ").split(',')
    marks = list(map(int, marks))
    students.append({"RollNo": roll_no, "Name": name, "Marks": marks})
    print("Student added successfully!\n")

def search_student():
    roll_no = input("Enter Roll No to search: ")
    for student in students:
        if student["RollNo"] == roll_no:
            print("Student Found:", student)
            return
    print("Student not found.\n")

def list_students():
    if not students:
        print("No students available.\n")
        return
    print("Lstudentsist of Students:")
    for student in students:
        print(student)
    print()

def update_student():
    roll_no = input("Enter Roll No to update: ")
    for student in students:
        if student["RollNo"] == roll_no:
            name = input("Enter new name (leave blank to keep same): ")
            marks = input("Enter new marks (comma separated, leave blank to keep same): ")
            if name:
                student["Name"] = name
            if marks:
                student["Marks"] = list(map(int, marks.split(',')))
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    for student in students:
        if student["RollNo"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

def menu():
    while True:
        print("Menu:")
        print("a) Add Student")
        print("b) Search Student")
        print("c) List All Students")
        print("d) Update Student")
        print("e) Delete Student")
        print("f) Exit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == 'a':
            add_student()
        elif choice == 'b':
            search_student()
        elif choice == 'c':
            list_students()
        elif choice == 'd':
            update_student()
        elif choice == 'e':
            delete_student()
        elif choice == 'f':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()

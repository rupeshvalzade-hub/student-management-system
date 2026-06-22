import json
import os

FILE_NAME = "students.json"

# Load student data
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save student data
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student():
    students = load_students()

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[roll_no] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    save_students(students)
    print("Student added successfully!")

# View students
def view_students():
    students = load_students()

    if not students:
        print("No student records found!")
        return

    print("\nStudent Records")
    print("-" * 40)

    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Course: {details['Course']}")
        print("-" * 40)

# Update student
def update_student():
    students = load_students()

    roll_no = input("Enter Roll Number to update: ")

    if roll_no not in students:
        print("Student not found!")
        return

    name = input("Enter New Name: ")
    age = input("Enter New Age: ")
    course = input("Enter New Course: ")

    students[roll_no] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    save_students(students)
    print("Student updated successfully!")

# Delete student
def delete_student():
    students = load_students()

    roll_no = input("Enter Roll Number to delete: ")

    if roll_no not in students:
        print("Student not found!")
        return

    del students[roll_no]
    save_students(students)

    print("Student deleted successfully!")

# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")    
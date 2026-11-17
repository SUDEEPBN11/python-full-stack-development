
class Student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("----------------------------")
        print("USN   :", self.usn)
        print("Name  :", self.name)
        print("Marks :", self.marks)
        print("----------------------------")


class StudentManagement:

    def __init__(self):
        self.students = []

    
    def add_student(self):
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(usn, name, marks)
        self.students.append(student)

        print("Student added successfully!")

    
    def display_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display()

    
    def search_student(self):
        usn = input("Enter USN to search: ")

        for student in self.students:
            if student.usn == usn:
                student.display()
                return

        print("Student not found!")


    def update_marks(self):
        usn = input("Enter USN to update marks: ")

        for student in self.students:
            if student.usn == usn:
                marks = float(input("Enter new marks: "))
                student.marks = marks
                print("Marks updated successfully!")
                return

        print("Student not found!")


    def delete_student(self):
        usn = input("Enter USN to delete: ")

        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

management = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        management.add_student()

    elif choice == "2":
        management.display_students()

    elif choice == "3":
        management.search_student()

    elif choice == "4":
        management.update_marks()

    elif choice == "5":
        management.delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

        




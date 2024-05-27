class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no}, Grade: {self.grade})"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)

    def get_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def display_students(self):
        for student in self.students:
            print(student)


def main():
    school = School("Sarkari School")

    while True:
        print("\n1. Add Student")
        print("2. Get Student")
        print("3. Display Students")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            roll_no = int(input("Enter student roll no: "))
            grade = input("Enter student grade: ")

            student = Student(name, roll_no, grade)
            school.add_student(student)

        elif choice == 2:
            roll_no = int(input("Enter roll no to get student: "))
            student = school.get_student(roll_no)

            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == 3:
            school.display_students()

        elif choice == 4:
            break

        else:
                    print("Invalid choice.")


if __name__ == "__main__":
    main()
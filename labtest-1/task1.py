class SRUStudent:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def Student_Data(self, filename="Student_Data.txt"):
        with open(filename, "a") as file:
            file.write(f"Name: {self.name}, Roll No: {self.roll_no}, Department: {self.department}\n")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Department: {self.department}")

# Example usage:
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")
    student = SRUStudent(name, roll_no, department)
    student.Student_Data()
    print("Student details saved to Student_Data.txt")
    print("Student details:")
    student.display()
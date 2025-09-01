class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def compute_grade(self):
        if self.marks > 90:
            grade = "A"
        elif self.marks > 75:
            grade = "B"
        elif self.marks > 60:
            grade = "C"
        else:
            grade = "Fail"
        print(f"Grade: {grade}")

# Example usage
if __name__ == "__main__":
    s1 = student("Alice", 101, 88)
    s1.display_details()
    s1.compute_grade()


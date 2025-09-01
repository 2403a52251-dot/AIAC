class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display_details(self):
        """Method to display student details"""
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

    def calculate_grade(self):
        """Method to calculate grade based on marks"""
        if self.marks > 90:
            return "A"
        elif self.marks > 75:
            return "B"
        elif self.marks > 60:
            return "C"
        else:
            return "Fail"


# Example usage
if __name__ == "__main__":
    # Create student objects
    student1 = student("John Doe", "2024001", 85)
    student2 = student("Jane Smith", "2024002", 95)
    student3 = student("Bob Johnson", "2024003", 45)
    
    # Display student details
    print("Student 1 Details:")
    student1.display_details()
    print("\nStudent 2 Details:")
    student2.display_details()
    print("\nStudent 3 Details:")
    student3.display_details()
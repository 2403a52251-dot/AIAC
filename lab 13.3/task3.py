class Student:
    """
    A class to represent a student with name, age, and marks.
    """
    
    def __init__(self, name, age, marks):
        """
        Initialize a Student object.
        
        Args:
            name (str): The student's name
            age (int): The student's age
            marks (list): List of student's marks
        """
        self.name = name
        self.age = age
        self.marks = marks
    
    def display_details(self):
        """
        Display student's basic information in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def calculate_total_marks(self):
        """
        Calculate the total marks of the student.
        
        Returns:
            int: Sum of all marks
        """
        return sum(self.marks)


# Example usage
if __name__ == "__main__":
    student = Student("John Doe", 20, [85, 92, 78])
    student.display_details()
    total = student.calculate_total_marks()
    print(f"Total Marks: {total}")
    print(f"Average: {total / len(student.marks):.2f}")

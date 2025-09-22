def welcome_student(student_name):
    """
    Print a welcome message for a student.

    Args:
        student_name (str): The name of the student.
    """
    print(f"Welcome {student_name}")

# List of students
students = ["Alice", "Bob", "Charlie"]

# Welcome each student
for student in students:
    welcome_student(student)

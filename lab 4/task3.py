def get_student_info():
    students = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        full_name = input("Full name: ")
        branch = input("Branch: ")
        sgpa = float(input("SGPA: "))
        students[full_name] = {
            "Branch": branch,
            "SGPA": sgpa
        }
    return students

# Example usage:
if __name__ == "__main__":
    student_data = get_student_info()
    print("\nStudent Information:")
    for name, info in student_data.items():
        print(f"Name: {name}, Branch: {info['Branch']}, SGPA: {info['SGPA']}")
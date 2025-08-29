class StudentRecord:
    def __init__(self, name, id, courses=None):
        # Fix mutable default argument issue
        if courses is None:
            courses = []
        
        # Fix variable name errors
        self.studentName = name  # was 'names'
        self.student_id = id
        self.courses = courses  # was 'courseList'

    def add_course(self, course):
        self.courses.append(course)

    def get_summary(self):
        return f"Student: {self.studentName}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"

class Department:
    def __init__(self, deptName, students=None):
        self.dept_name = deptName
        # Fix initialization of students list
        if students is None:
            self.students = []
        else:
            self.students = students

    def enroll_student(self, student):
        self.students.append(student)

    def department_summary(self):
        # Fix attribute name error
        return f"Department: {self.dept_name}, Total Students: {len(self.students)}"  # was 'self.student'
        

# Test the classes
s1 = StudentRecord("Alice", 101, ["Math", "Science"])
s2 = StudentRecord("Bob", 102)  # Test with no courses initially
s2.add_course("Physics")  # Test adding a course

d1 = Department("Computer Science")
d1.enroll_student(s1)
d1.enroll_student(s2)

print("Student Records:")
print(s1.get_summary())
print(s2.get_summary())
print("\nDepartment Summary:")
print(d1.department_summary())

# Test with multiple departments
d2 = Department("Mathematics", [s1])  # Test with initial students
print(f"\nSecond Department: {d2.department_summary()}")


# College Management System using Python OOP

class Student:
    def __init__(self, roll_no, name, student_class):
        self.roll_no = roll_no
        self.name = name
        self.student_class = student_class  # class/department name

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Class: {self.student_class}"


class Instructor:
    def __init__(self, instructor_id, name, subject):
        self.instructor_id = instructor_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Instructor ID: {self.instructor_id}, Name: {self.name}, Subject: {self.subject}"


class Course:
    def __init__(self, course_code, course_name, fee):
        self.course_code = course_code
        self.course_name = course_name
        self.fee = fee

    def __str__(self):
        return f"{self.course_code} - {self.course_name}, Fee: {self.fee}"


class College:
    def __init__(self, name, principal, vice_principal):
        self.name = name
        self.principal = principal
        self.vice_principal = vice_principal
        self.departments = []
        self.instructors = []
        self.students = []
        self.courses = []

    # Add data
    def add_department(self, department_name):
        self.departments.append(department_name)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    # Show info
    def show_college_info(self):
        print(f"\n🏫 College: {self.name}")
        print(f"Principal: {self.principal}")
        print(f"Vice Principal: {self.vice_principal}")
        print(f"Departments: {', '.join(self.departments)}")
        print(f"Total Instructors: {len(self.instructors)}")
        print(f"Total Students: {len(self.students)}")
        print(f"Courses Offered: {len(self.courses)}")

    def show_students(self):
        print("\n👨‍🎓 Students List:")
        for student in self.students:
            print(student)

    def show_instructors(self):
        print("\n👩‍🏫 Instructors List:")
        for instructor in self.instructors:
            print(instructor)

    def show_courses(self):
        print("\n📚 Courses Offered:")
        for course in self.courses:
            print(course)

    def show_fee_structure(self):
        print("\n💰 Fee Structure:")
        for course in self.courses:
            print(f"{course.course_name}: {course.fee}")


# ------------------- DEMO -------------------
if __name__ == "__main__":
    # Create a college
    my_college = College("RealEste College", "Dr. John Smith", "Prof. Alice")

    # Add departments
    my_college.add_department("Computer Science")
    my_college.add_department("Business")
    my_college.add_department("Mathematics")

    # Add instructors
    my_college.add_instructor(Instructor(1, "Mr. David", "Python Programming"))
    my_college.add_instructor(Instructor(2, "Ms. Emily", "Business Management"))

    # Add students
    my_college.add_student(Student(101, "Waheed Abbas", "Computer Science"))
    my_college.add_student(Student(102, "Ali Raza", "Business"))
    my_college.add_student(Student(103, "Sara Khan", "Mathematics"))

    # Add courses
    my_college.add_course(Course("CS101", "Python Programming", 30000))
    my_college.add_course(Course("BUS201", "Business Management", 25000))
    my_college.add_course(Course("MATH301", "Advanced Calculus", 28000))

    # Show all details
    my_college.show_college_info()
    my_college.show_students()
    my_college.show_instructors()
    my_college.show_courses()
    my_college.show_fee_structure()

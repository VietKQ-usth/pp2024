class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
    def get_dob(self):
        return self.__dob
    def set_dob(self, dob):
        self.__dob = dob
    

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        

class StudentMark:
    def __init__(self, course_id, student_id, score):
        self.__course_id = course_id
        self.__student_id = student_id
        self.__score = score

    def get_course_id(self):
        return self.__course_id
    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_student_id(self):
        return self.__student_id
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
        

def input_students():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Student Date of Birth (dd/mm/yyyy): ")
        students.append(Student(id, name, dob))
    return students


def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append(Course(id, name))
    return courses


def input_marks(students, courses):
    marks = []
    for course in courses:
        print(f"Entering marks for course: {course.get_name()} (ID: {course.get_id()})")
        for student in students:
            score = float(input(f"Enter marks for student {student.get_name()} (ID: {student.get_id()}): "))
            marks.append(StudentMark(course.get_id(), student.get_id(), score))
    return marks


def list_courses(courses):
    print("\nCourses:")
    for course in courses:
        print(f"ID: {course.get_id()}, Name: {course.get_name()}")


def list_students(students):
    print("\nStudents:")
    for student in students:
        print(f"ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")


def list_marks(course_id, marks):
    print(f"\nMarks for Course ID: {course_id}")
    for mark in marks:
        if mark.get_course_id() == course_id:
            print(f"Student ID: {mark.get_student_id()}, Score: {mark.get_score()}")


# Main program
students = input_students()
courses = input_courses()
marks = input_marks(students, courses)

list_courses(courses)
list_students(students)
course_id = input("\nEnter Course ID to view marks: ")
list_marks(course_id, marks)

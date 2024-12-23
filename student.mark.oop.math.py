import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        # __ for private, _ for protected
        self.__id= id
        self.__name= name
        self.__dob= dob
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id= id

    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name= name
    
    def get_dob(self):
        return self.__dob
    def set_dob(self, dob):
        self.__dob= dob
    

class Course:
    def __init__(self, id, name):
        self.__id= id
        self.__name= name
        self.__marks = {}
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id= id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name= name

    def add_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_marks(self):
        return self.__marks
        

class StudentMark:
    def __init__(self, course_id, student_id, score):
        self.__course_id= course_id
        self.__student_id= student_id
        self.__score= score

    def get_course_id(self):
        return self.__course_id
    def set_course_id(self, course_id):
        self.__course_id= course_id

    def get_student_id(self):
        return self.__student_id
    def set_student_id(self, student_id):
        self.__student_id= student_id

    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score= score

class StudentMarkManagement:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__marks = []

    def hardcoded_data(self):
        # Hardcoded students
        self.__students = {
            "202412": Student("202412", "John Doe", "29/10/2004"),
            "202411": Student("202411", "Jane Smith", "07/03/2004")
        }

        # Hardcoded courses
        self.__courses = {
            "M2.001": Course("M2.001", "Maths"),
            "M2.002": Course("M2.002", "Calculus")
        }

        # Hardcoded marks
        self.__courses["M2.001"].add_mark("202412", 18.0)
        self.__courses["M2.001"].add_mark("202411", 15.5)
        self.__courses["M2.002"].add_mark("202412", 20.0)
        self.__courses["M2.002"].add_mark("202411", 17.0)

    def calculate_gpa(self):
        course_credits = {course.get_id(): 3 for course in self.__courses.values()}  # Assume equal credits for simplicity
        for student_id, student in self.__students.items():
            total_scores = 0
            total_courses = 0
            for course in self.__courses.values():
                if student_id in course.get_marks():
                    total_scores += course.get_marks()[student_id]
                    total_courses += 1
            gpa = total_scores / total_courses if total_courses > 0 else 0
            print(f"GPA for {student.get_name()} (ID: {student.get_id()}): {gpa:.2f}")

    def sort_students_by_gpa(self):
        students_with_gpa = []
        for student_id, student in self.__students.items():
            total_scores = 0
            total_courses = 0
            for course in self.__courses.values():
                if student_id in course.get_marks():
                    total_scores += course.get_marks()[student_id]
                    total_courses += 1
            gpa = total_scores / total_courses if total_courses > 0 else 0
            students_with_gpa.append((student, gpa))
        sorted_students = sorted(students_with_gpa, key=lambda x: x[1], reverse=True)
        print("\nStudents sorted by GPA:")
        for student, gpa in sorted_students:
            print(f"{student.get_name()} (ID: {student.get_id()}) - GPA: {gpa:.2f}")

    def list_courses(self):
        print("\nCourses:")
        for course in self.__courses.values():
            print(f"ID: {course.get_id()}, Name: {course.get_name()}")

    def list_students(self):
        print("\nStudents:")
        for student in self.__students.values():
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.hardcoded_data()

    print("\nListing courses:")
    smm.list_courses()

    print("\nListing students:")
    smm.list_students()

    print("\nCalculate and display GPA:")
    smm.calculate_gpa()

    print("\nSort students by GPA:")
    smm.sort_students_by_gpa()


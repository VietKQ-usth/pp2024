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
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id= id

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name= name
        

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
        
def student_num():
    return int(input("The number of students: "))
    
def course_num():
    return int(input("The number of courses: "))
    
def list_course(courses):
    for course in courses:
        print("Course ID: "+ str(course.get_id()))
        print("Course name: "+ str(course.get_name()))
        
def list_student(students):
    for student in students:
        print("Student ID: "+ str(student.get_id()))
        print("Student name: "+ str(student.get_name()))
        print("DoB: "+ str(student.get_dob()))
            
def list_mark(course_id, marks):
    print("Course ID: "+ course_id)
    for mark in marks:
        if str(mark.get_course_id()) == course_id: 
            print("Student ID: "+ str(mark.get_student_id()))
            print("Mark: "+ str(mark.get_score()))

student_1 = Student("202412","Nigga","29/10/2004")
student_2 = Student("202411", "Big", "07/03/2004")
students = [student_1, student_2]

course_1= Course("M2.001", "Maths")
course_2= Course("M2.002", "Calculus")
courses= [course_1, course_2]

mark_1= StudentMark("M2.001", "202412", 20)
mark_2= StudentMark("M2.001", "202411", 20)
mark_3= StudentMark("M2.002", "202412", 20)
mark_4= StudentMark("M2.002", "202411", 20)
marks= [mark_1, mark_2, mark_3, mark_4]

student_num()
course_num()
list_course(courses)
list_student(students)
list_mark("M2.002", marks)
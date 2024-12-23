def student_num():
    return int(input("Number of students: "))
def student_info(id):
    name = str(input("Name of student: "))
    DoB = str(input("DoB of student: "))
    student = {'ID': id, 'Name': name, 'DoB': DoB}
    return student
def course_num():
    return int(input("The number of courses: "))
def course_info(id):
    name = str(input("Name of the course: "))
    course = {'ID': id, 'Name': name}
    return course

def score(course_id, student_id):
    mark = int(input("Mark of the student in this course: "))
    score = {'Student ID': student_id, 'Course ID': course_id, 'Mark': mark}
    return score

def list_course(courses):
    for course in courses:
        print("Course ID: "+ course['ID'])
        print("Course name: "+ course['Name'])

def list_student(students):
    for student in students:
        print("Student ID: "+ student['ID'])
        print("Student name: "+ student['Name'])
        print("DoB: "+ student['DoB'])

def list_mark(course_id, marks):
    print("Course ID: "+ course_id)
    for mark in marks:
        if mark['Course ID'] == course_id: 
            print("Student ID: "+ mark['Student ID'])
            print("Mark: "+ str(mark['Mark']))

student_num()
student1 = student_info("202412")
student2 = student_info("202415")
students= [student1, student2]

course_num()
course1= course_info("SCI3.1")
course2= course_info("MAT1.2")
courses= [course1, course2]

mark1= score("SCI3.1", "202412")
mark2= score("SCI3.1", "202415")
mark3= score("MAT1.2", "202412")
mark4= score("MAT1.2", "202415")
marks= [mark1, mark2, mark3, mark4]

list_course(courses)
list_student(students)
list_mark("MAT2.1", marks)
list_mark("SCI3.1", marks)

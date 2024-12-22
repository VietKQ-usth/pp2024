import numpy as np
import math

class Course:
    def __init__(self):
        midterm = 0
        final = 0
        attendant = 0
        cour_id = 0
    def score(self):
        overall = math.floor(float(0.1 * self.attendant + 0.4 * self.midterm + 0.5 * self.final))
        return overall

#Student inherits Course class
class Student(Course):
    student_list = [] #create a list of student to later show every student information
    __name = ""
    age = 0
    __id = 0
    
    def __init__(self):
        super().__init__()
        Student.student_list.append(self) #the student list will add new student information whenever a new student is created
    
    def setname(self,name):
        self.__name = name
    
    def getname(self):
        return self.__name
    
    def setid(self,id):
        self.__id = id
    
    def getid(self):
        return self.__id
    
    def display(self):
        print("\nStudentName", self.__name, "age", self.age, "id", self.__id, "Course",self.cour_id, "mark", self.midterm,"-", self.final,"-", self.attendant, "Overall", self.score() )
                     #the mark is private for only Course class, so if I want to get it for display i need to call the getter method
                     
    def input(self, name, age, id, cour_id, midterm, final, attendant):
        self.setname(name)
        self.age = age
        self.setid(id)
        self.cour_id = cour_id
        self.midterm = midterm
        self.final = final
        self.attendant = attendant
        
    @classmethod #special method to be used by directly calling the class
    def showAll(Student):
        sorted_score = sorted(Student.student_list, key=lambda student: student.score(), reverse=True) #use sorted function to sort by the score
        for student in sorted_score:
            student.display()

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()

student1.input("A", 20, 1, 1, 20, 10, 2)
student2.input("B", 18, 2, 1, 6, 6, 4)
student3.input("C", 19, 3, 1, 10, 20, 20)
student4.input("D", 21, 4, 1, 16, 7, 1)
student5.input("E", 20, 5, 1, 1, 2, 3)

Student.showAll()


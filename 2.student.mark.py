class Course:
    def __init__(self):
        __mark = 0
        cour_id = 0
    def setMark(self,mark):
        self.__mark = mark
    def getMark(self):
        return self.__mark

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
        print("\nStudentName", self.__name, "age", self.age, "id", self.__id, "Course",self.cour_id, "mark", self.getMark() )
                     #the mark is private for only Course class, so if I want to get it for display i need to call the getter method
                     
    def input(self, name, age, id, cour_id, mark):
        self.setname(name)
        self.age = age
        self.setid(id)
        self.cour_id = cour_id
        self.setMark(mark)
        
    @classmethod #special method to be used by directly calling the class
    def showAll(Student):
        for student in Student.student_list:
            student.display()

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()

student1.input("A", 20, 1, 1, 20)
student2.input("B", 18, 2, 1, 6)
student3.input("C", 19, 3, 1, 10)
student4.input("D", 21, 4, 1, 16)
student5.input("E", 20, 5, 1, 1)

Student.showAll()

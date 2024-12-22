import random

student  = ["A", "B", "C", "D", "E", "F"]
id = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6
}
mark = []
dob = []

#adding new student to the list
student.append("G")
student.append("H")

#adding new id to the dict
id["G"] = 7
id["H"] = 8

for i in range(1, len(student)+1):
    mark.append( random.randint(1, 20))

print("List of all scores: \n")
for i in range (len(student)):
    print(mark[i], sep = " ", end = " ")
    
print("\nPlease input which student you want to check: ")
x = input()
print("The score for the student you want is:", mark[int(id[x]-1)])



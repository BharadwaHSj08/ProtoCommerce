class Students:

    def setName(self,name):
        self.name = name

    def setMarks(self,marks):
        self.marks = marks

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks

n = int(input("Enter students count:"))

students_list = []

for i in range(n):
    s= Students()
    name = input("Enter Name:")
    marks = float(input("Enter marks:"))

    s.setName(name)
    s.setMarks(marks)
    students_list.append(s)

for each_student in students_list:
    print("Hi", each_student.getName())
    print("Your marks are:",each_student.getMarks())
    print()






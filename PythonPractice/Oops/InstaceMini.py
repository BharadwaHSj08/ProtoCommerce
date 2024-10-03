class Students:

    college_name = "BIET"

    def __init__(self,studentName,marks):
        self.marks = marks
        self.studentName = studentName

    def info(self):
        print("Marks obtained are:", self.marks)

    def grade(self):
        if self.marks >= 60:
            print("A Grade")

        elif self.marks >= 50:
            print("B Grade")

        elif self.marks >= 35:
            print("C Grade")

        else:
            print("Fail")

print("The Results are for College :", Students.college_name)

n = int(input("Enter number of Students:"))

for i in range(n):

    studentname = input("Enter the Name:")
    marks = float(input("Enter marks:"))
    s = Students(studentname,marks)
    s.info()
    s.grade()
    print()





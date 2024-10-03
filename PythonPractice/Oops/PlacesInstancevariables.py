class Student:
    school_number = 20

    def __init__(self):
        Student.b = 30
        print(Student.b)

    def m1(self):
        Student.c = 40

    @classmethod
    def getInfo(cls):
        cls.d = 50
        Student.e = 60

    @staticmethod
    def getSum():
        return Student.d + Student.e


s=Student()
s.m1()
s.getInfo()
s.getSum()
Student.g = 70
print(Student.__dict__)


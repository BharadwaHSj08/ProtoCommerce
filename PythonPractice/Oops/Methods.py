class Student:

    school_name = "Chaitanya"

    def __init__(self,name,RollNo):
        self.name = name
        self.RollNo = RollNo

    def getStudentInfo(self):
        s = f"Student name is {self.name}, Roll Number is {self.RollNo}"
        return s

    @classmethod
    def getSchoolName(cls):
        d=f"the name of school is {cls.school_name}"
        return d

    @staticmethod
    def getSum(a,b):
        sum = a+b
        return sum

o = Student("Ram",21)

print(o.getStudentInfo())
print(o.getSum(10,20))
print(o.getSchoolName())
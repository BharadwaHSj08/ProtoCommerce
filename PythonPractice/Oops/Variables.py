class Student:

    school_name = "Chaitanya School"  #Static Variable(class level)

    def __init__(self,name,RollNo):
        self.name = name        #Instance Variables(Object Level)
        self.RollNo = RollNo    #Instance Variables(Object Level)

    def info(self):
        s=f"My Name is {self.name},  My Roll is {self.RollNo}, My school is {Student.school_name}"
        return s

    def add(self):
        a = 10  #Local variables(Method Level)
        b = 10  #Local Variables(Method Level)
        return a+b


s = Student("Bharat",21)
print(s.info())
print(s.add())




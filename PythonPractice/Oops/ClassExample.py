class Student:

    out_off = 100

    #def __init__(self,name,Roll,marks):
    #    self.name = name
    #    self.Roll = Roll
    #    self.marks = marks

    def talk(self,name,Roll,marks):
        print(f"My Name is {name}, My Roll is {Roll}, My marks are {marks}, Total marks are {Student.out_off}")

s=Student()
s2=Student()
s.talk("Bharat",20,95)
s2.talk("Aparna",21,99)


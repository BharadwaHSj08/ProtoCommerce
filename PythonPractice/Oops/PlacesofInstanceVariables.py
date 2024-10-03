class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30

t=Test()
t.m1()
t.d=40
#To access the instance variables outside the class
print(t.a)
#To update the instance variables

t2=Test()
print(t.__dict__)
print(t2.__dict__)
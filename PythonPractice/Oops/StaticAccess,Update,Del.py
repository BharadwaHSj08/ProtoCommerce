class Test:

    a = 10
    b = 20
    c = 30
    h = 2

    new_c = a + 1

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def info(cls):
        print(cls.a)
        print(Test.a)
        print(cls.new_c)

    @classmethod
    def update(cls,f):
        cls.h = f

    @staticmethod
    def stat():
        print(Test.a)


t = Test()
t.m1()
t.info()
t.stat()
t.update(22)
print(t.a)
print(Test.a)
Test.d = 40
print(Test.__dict__)
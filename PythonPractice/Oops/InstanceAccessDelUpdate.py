class Test:

    def __init__(self):
        self.a = 10
        self.b = 20

    def accessinClass(self):
        print(self.a)
        self.c=30

t=Test()
t.accessinClass()
print(t.b)
t.b=40
print(t.__dict__)
del t.c
print(t.__dict__)
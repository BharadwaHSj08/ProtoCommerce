class Overload:

    def add(self,a,b,c):
        return a+b+c

    def add(self,a,b,c,d):
        return a+b+c+d

o = Overload()
print(o.add(1,2,3,0))
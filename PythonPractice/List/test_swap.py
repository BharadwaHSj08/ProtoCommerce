class TestSwap:

    def swapTwo(self,list1,a,b):
        self.a = a
        self.b = b

        first_index = list1.index(self.a)
        second_index = list1.index(self.b)

        list1[first_index] = b
        list1[second_index] = a

        return list1


t= TestSwap()
list1=[10,20,30,40]
swapping = t.swapTwo(list1, 20 , 40)
print(swapping)



list1 = [10,20,30,40]

#a = int(input("Enter first number:"))
#b = int(input("Enter second number:"))

a = 20
b = 40

first_index = list1.index(a)
second_index = list1.index(b)

list1[first_index] = b
list1[second_index] = a
print(list1)
print(first_index)
print(second_index)
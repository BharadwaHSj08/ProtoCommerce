input_string = "One Two Three Four Five Six"

input_list = input_string.split(" ")

print(input_list)
list=[]

for item in input_list:
    if input_list.index(item) % 2 == 0:
        list.append(item)
    else:
        list.append(item[::-1])
print(' '.join(list))
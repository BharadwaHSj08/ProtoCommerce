input_string = "learning Python is Easy"

input_list = input_string.split(" ")
print(input_list)
reversed_list = []

for item in input_list:
    output = item[::-1]
    reversed_list.append(output)

print(' '.join(reversed_list))
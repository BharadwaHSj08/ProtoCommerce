input_string="Hello, I am Bharadwaj and i am a software engineer"

input_list = input_string.split(" ")
print(input_list)
even_list =[]
odd_list =[]
for char in input_list:
    if input_list.index(char) % 2 == 0:
        even_list.append(char)
    else:
        odd_list.append(char)

print(' '.join(even_list))
print(' '.join(odd_list))
input_string= "a4b3c2"
#output :aaaabbbcc

output=""
for char in input_string:
    if char.isalpha():
        x = char
    else:
        y = int(char)
        output = output +x * y
print(output)


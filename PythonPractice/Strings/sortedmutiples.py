input_string= "a3z2b4"
#output :aaabbbbzz

output=""
for char in input_string:
    if char.isalpha():
        x = char
    else:
        y = int(char)
        output = output +x * y
sort_output = sorted(output)
print(''.join(sort_output))
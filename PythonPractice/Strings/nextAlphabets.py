input_string = "a4k3b2"
#output : "aeknbd"

output =""

for char in input_string:
    if char.isalpha():
        output = output + char
        x = char

    else:
        d = int(char)
        new_charac = chr(ord(x) + d)
        output = output + new_charac

print(output)

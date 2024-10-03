input_string="xaaaabbbccz"
#output:"4a3b2c1z

output = ""
i = 0
for char in input_string:
    if char == input_string[i]:
        occurence = input_string.count(char)
        output = output + str(occurence) + char
        i = i + occurence
    else:
        i = i

print(output)
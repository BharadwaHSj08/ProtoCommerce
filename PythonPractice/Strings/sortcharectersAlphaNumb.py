input_string="B4A1D3"
#op :ABD134

aplpha =""
num =""
for char in input_string:
    if char.isnumeric():
        num += char
    else:
        aplpha += char

print(''.join(sorted(aplpha) + sorted(num)))
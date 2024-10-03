input_1 = "abcdefg"
input_2 = "xyz"
input_3 = "12345"
#output = ax1 , by2, cz3, d4, e5, f,g
i=j=k=0
output=""

while i < len(input_1) or j < len(input_2) or k < len(input_3):
    if i < len(input_1):
        output = output + input_1[i]
        i += 1

    if j < len(input_2):
        output = output + input_2[j]
        j += 1

    if k < len(input_3):
        output = output + input_3[k] + ","
        k += 1
print(output)
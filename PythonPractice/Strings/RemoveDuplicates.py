input_string= "ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF"
#output : AZBCDEF

new_string = set(input_string)

print(''.join(new_string))
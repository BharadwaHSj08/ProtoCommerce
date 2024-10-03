input_string = "ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF"
sorted_str = sorted(input_string)
list_1 = []
output = ""
Dict={}
for char in sorted_str:
    occurence = input_string.count(char)
    list_1.append(char)
    output = output + "{} is repeated {} times,".format(char,occurence)
    Dict[char] = occurence
print(output)
print(Dict)
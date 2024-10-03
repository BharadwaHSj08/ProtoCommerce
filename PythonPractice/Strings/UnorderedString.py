input_string = "ABAABBCA"
#output : 4A3B1C
Dict={}
output=""

for char in sorted(input_string):
    Dict[char] = Dict.get(char,0)+1
print(Dict)

for k,v in Dict.items():
    output = output + str(v)+k

print(output)
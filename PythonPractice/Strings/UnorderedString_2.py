input_string = "ABAABBCA"
#output : A4B3C1
Dict={}
output=""

for char in sorted(input_string):
    Dict[char] = Dict.get(char,0)+1
print(Dict)

for k,v in Dict.items():
    output = output +k + str(v)

print(output)
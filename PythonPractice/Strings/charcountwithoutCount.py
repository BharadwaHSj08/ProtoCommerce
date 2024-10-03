input_string = "AAAAABBBBCCCCCCD"

Dict = {}

for char in input_string:
    Dict[char] = Dict.get(char,0) + 1

print(Dict)
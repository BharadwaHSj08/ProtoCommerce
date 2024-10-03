input_string = input("Enter the String:")
vowels =['a','e','i','o','u','A','E','I','O','U']
Dict={}

for char in input_string:
    if char in vowels:
        Dict[char] = Dict.get(char,0)+1

for k,v in Dict.items():
    print("{} repeated {} times".format(k,v))


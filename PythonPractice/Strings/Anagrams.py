input_string_1 = "lazy"
input_string_2 = "zaly"

#Two Strings are said to be Anagrams iff both are having same content irrespective of the Character positions.

if sorted(input_string_1) == sorted(input_string_2):
    print("The Strings are Anagrams")
else:
    print("The Strings are not Anagrams")


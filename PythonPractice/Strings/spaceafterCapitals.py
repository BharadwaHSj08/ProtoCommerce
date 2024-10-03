input_str = "HelloIAmBharadwaj"

output=("")

for char in input_str:
    if char.isupper():
        output = output + " " + char
    else:
        output = output + char

print(output.strip())
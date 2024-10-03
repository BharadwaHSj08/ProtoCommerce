string = "Bharadwaj"
list = []
for i in range(len(string)):
    list.append(string[-i-1])

print(''.join(list))
a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [x + 2 for x in a]
c = set(b[1:6])

print("Original array: ",a[:])
print("New array: ",c)
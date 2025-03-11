a = input()
b = ''

for i in a:
    if i.islower():
        b += i.upper()
    else:
        b += i.lower()

    print(b)
a = int(input("Give me the first number : "))
b = int(input("Give me the second number : "))

print("Thank you!")

c = ["+","-","/","*"]

for i in range(1,5):
    print(f"{a} {c[i-1]} {b} = {eval(f'{a} {c[i-1]} {b}')}")
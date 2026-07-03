ki=int(input("Enter Input:"))

for i in range(1, ki + 1):
    for j in range(ki - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()
for i in range(ki - 1, 0, -1):
    for j in range(ki - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print() 
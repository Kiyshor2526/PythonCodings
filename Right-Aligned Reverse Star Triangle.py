Sum = int(input("Enter Input:"))

for i in range(Sum,0,-1):
    for j in range(Sum-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
        
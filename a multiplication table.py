n=int(input("Enter a number: "))
print("The multiplication table of", n, "is:")
for i in range(1, 11):  
    result = i*n
    print(n, "x", i, "=", result)             
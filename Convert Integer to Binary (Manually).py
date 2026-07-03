n = int(input("Enter an integer: "))

binary = ""

while n > 0:
    rem = n % 2
    binary = str(rem) + binary
    n = n//22

print("Binary value is:", binary)

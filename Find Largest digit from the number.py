Kii = int(input("Enter a number: "))

largest = 0

while Kii > 0:
    digit = Kii % 10
    if digit > largest:
        largest = digit
    Kii = Kii // 10

print("The largest digit in the number is:", largest)
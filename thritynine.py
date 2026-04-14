


num = int(input("Enter a number: "))

mul = 1

while num > 0:
    digit = num % 10
    mul = mul * digit
    num = num // 10

print("Product of digits is:", mul)
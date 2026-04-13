
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter an operator: ")

if op == "+":
    result = a + b
    print("The sum is:", result)
elif op == "-":
    result = a - b
    print("The difference is:", result)
elif op == "*":
    result = a * b
    print("The product is:", result)
elif op == "/":
    result = a / b
    print("The quotient is:", result)
else:
    print("Invalid operator.")

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    #the spaces

    for j in range(i):
        print(" ", end="")

    #the stars

    for j in range(num-i):
        print("*", end="")

    print()

print("Done!")

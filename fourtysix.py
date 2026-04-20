

num = int(input("Enter a number: "))

for i in range(1, num + 1):

    #spaces
    for j in range(num-i):
        print(" ", end=" ")
    
    #stars
    for j in range(1, i + 1):
        print("*", end=" ")

    print()

print("Pattern printed.")
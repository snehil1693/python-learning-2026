
# reverse pyramid
# spaces = i
# stars = 2*(n-i) - 1

num = int(input("Enter a number: "))

for i in range(num):

    #the spaces

    for j in range(i):
        print(" ", end="")

    #the stars

    for j in range(2*(num - i) - 1):
        print("*", end="")

    print()

print("Done!")

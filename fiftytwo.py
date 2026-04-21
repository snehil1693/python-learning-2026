
# space + stars
# spaces = n - i
# stars = 2*i - 1

num = int(input("Enter a number: "))

for i in range(1, num + 1):

    #the spaces

    for j in range(num -i):
        print(" ", end="")

    #the stars

    for j in range(2*i - 1):
        print("*", end="")

    print()

print("Done!")
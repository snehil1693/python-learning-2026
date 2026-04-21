

# Triangle -> Stars = i
# Pyramid -> Stars = 2*i -1
# Reverse -> decrease
# Diamond -> combine both

# in diamond, we have top as increasing stars and bottom as decreasing stars

num = int(input("Enter a number: "))

#upper part of diamond

for i in range(1, num + 1):

    # the spaces

    for j in range(num -i):
        print(" ", end="")

    # the stars

    for j in range(2*i - 1):
        print("*", end="")

    print()

#lower part of diamond

for i in range(num -1, 0, -1):

    # the spaces

    for j in range(num -i):
        print(" ", end="")

    # the stars

    for j in range(2*i - 1):
        print("*", end="")

    print()

print("Done!")


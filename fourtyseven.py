
row = int(input("Enter the number of rows: "))
stars = int(input("Enter the number of stars: "))

for i in range(1, row +1):
    for j in range(1, stars +1):
        print("*", end="")
    print()

print("Done!")
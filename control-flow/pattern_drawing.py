number = int(input("Enter the size of the pattern:"))
count = 0
while count < number:
    for j in range(number):
        print("*", end="")
    print()
    count += 1

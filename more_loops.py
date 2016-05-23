# Print 10, 5, and then 20 asterisks on different lines
for i in range(10):
        print("*", end=" ")
print()
for i in range(5):
    print("*", end=" ")
print()
for i in range(20):
    print("*", end=" ")

# Add whitespace
print()
print()
print()

# Print a 10 x 10 square of asterisks
for row in range(10):
    for column in range(10):
        print("*", end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print a 5 x 10 rectangle of asterisks
for row in range(10):
    for column in range(5):
        print("*", end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print a 20 x 5 rectangle of asterisks
for row in range(5):
    for column in range(20):
        print("*", end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print numbers 0 - 9 into 10 x 10 square
for i in range(10):
    for j in range(10):
        print(j, end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print numbers 0 - 9 on their own row in 10 x 10 square
for i in range(10):
    for j in range(10):
        print(i, end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print 10 rows of numbers, increasing row length by one each time
for i in range(10):
    for j in range(i + 1):
        print(j, end=" ")

    print()

# Add whitespace
print()
print()
print()

# Print 10 rows of numbers, decreasing row length by one each time
for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for j in range(10 - i):
        print(j, end=" ")

    print()

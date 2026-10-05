# Numbers Pattern
# Increasing Numbers Pattern
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Same Numbers Pattern
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

# Decreasing Numbers Pattern
n = 4

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# One Numbers Pattern
n = 4

for i in range(1, n + 1):
    for j in range(i):
        print(1, end="")
    print()

# Continuous Numbers Pattern
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Floyd's Triangle Pattern
c = 1
for i in range(1, n + 1):
    for j in range(i):
        print(c, end="")
        c += 1
    print()

# Pascal's Triangle Pattern
n = 5

for i in range(n):
    num = 1

    # spaces
    for space in range(n - i):
        print(" ", end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

# Alphabet Pattern
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# Repeating Alphabet Pattern
n = 5

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()

# Continues Alphabet Pattern
n = 5
ch = 65

for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
    print()
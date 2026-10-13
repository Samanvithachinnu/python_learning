# 1. List Comprehension - for

a = []
for x in range(1, 11):
    a.append(x)
print(a)

# Using List Comprehension
a = [x for x in range(1, 11)]
print(a)


# 2. List Comprehension - for-if

a = []
for x in range(1, 11):
    if x % 2 == 0:
        a.append(x)
print(a)

# Using List Comprehension
a = [x for x in range(1, 11) if x % 2 == 0]
print(a)


# 3. List Comprehension - for-if-for-if

a = []
for x in range(1, 5):
    if x % 2 == 0:
        for y in range(1, 4):
            if x + y == 5:
                a.append((x, y))
print(a)

# Using List Comprehension
a = [
    (x, y)
    for x in range(1, 5)
    if x % 2 == 0
    for y in range(1, 4)
    if x + y == 5
]
print(a)


# 4. Set Comprehension - Even numbers from 1 to 20

even_set = {x for x in range(1, 21) if x % 2 == 0}
print(even_set)


# 5. Dictionary Comprehension - Numbers and their squares

square_dict = {x: x ** 2 for x in range(1, 11)}
print(square_dict)


# 6. Function

def numbers():
    return 1
    return 2

n = numbers()
print(n)
print(type(n))


# 7. Generators

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4

n = numbers()
print(n)
print(type(n))

print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())


# 8. Generator - Even Numbers

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x

n = evennumbers()

print(next(n))
print(n.__next__())

for x in n:
    print(x)
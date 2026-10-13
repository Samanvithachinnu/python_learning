# 1. Normal Function
def add(x, y):
    return x + y

print(add(10, 20))
print(type(add))


# 2. Lambda Function
a = lambda x, y: x + y
print(a(10, 20))
print(type(a))


# 3. Lambda Function
b = lambda x, y: x + y
print(b(10, 20))


# 4. Lambda Function
c = lambda x, y: x + y
print(c(10, 20))


# 5. Lambda Function to Return Sum of Two Numbers
sum_numbers = lambda x, y: x + y
print(sum_numbers(10, 20))


# 6. Lambda Function to Return Square of a Number
square = lambda x: x ** 2
print(square(5))


# 7. Lambda Function to Return Second Element
second_element = lambda x: x[1]
print(second_element([10, 20, 30]))


# 8. Tricky Lambda Function
a = lambda x: print(x + 10)
print(a)
print(type(a))
a(10)


# 9. Map Function
numbers = [1, 2, 3, 4, 5, 6]

m = map(lambda x: x ** 2, numbers)
print(m)
print(type(m))

l = list(m)
print(l)


# 10. Filter Function
numbers = [1, 2, 3, 4, 5, 6]

f = filter(lambda x: x % 2 == 0, numbers)
print(f)
print(type(f))

l = list(f)
print(l)


# 11. Reduce Function
import functools

numbers = [1, 2, 3, 4, 5]

r = functools.reduce(lambda x, y: x + y, numbers)
print(r)
print(type(r))
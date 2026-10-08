# Local and Global Variables

a = 1   # Global variable
b = 2   # Global variable
c = 3   # Global variable

def f1():
    x = 10   # Local variable of f1()
    print(a)
    print(b)
    print(c)
    print(x)

def f2():
    y = 20   # Local variable of f2()
    print(a)
    print(b)
    print(c)
    print(y)

f1()
f2()

print(a)
print(b)
print(c)

#call by value, call by reference
# call by value 
def f1(a):
    a = 100
a = 4
f1(a)
print(a)      

#call by reference
def f2(a):
    a = [10, 20, 30]
    a[2] = 200
a = [1, 2, 3]
f2(a)
print(a)    

def f3(a):
    a[2] = 200
a = [1, 2, 3]
f3(a)
print(a)    

# recursive funcntions
# factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial =", result)

# fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")
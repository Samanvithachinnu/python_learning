#FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line
for i in range(1, 11):
    print(i, end=" ")

#2. print even numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end=" ")

#3. print odd numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end=" ")

#4. print numbers divisible by 5 from 1 to 30 in one line
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end=" ")

#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for i in range(1, 100):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")

#6. sum of numbers from 10 to 25 
sum = 0

for i in range(10, 26):
    sum = sum + i

print("Sum =", sum)

#7. sum of numbers in any list
numbers = [10, 20, 30, 40, 50]
sum = 0

for i in numbers:
    sum = sum + i

print("Sum =", sum)

#8. multiplication table of a number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#interview problems
#9. factorial 
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

#10. fibonacci 
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#11. reverse a string
s = input("Enter a string: ")

reverse = s[::-1]

print("Reverse =", reverse)

#12. count vowels in a string
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels =", count)

#13. count z's and y's in a string
s = input("Enter a string: ")

z_count = 0
y_count = 0

for ch in s:
    if ch in "zZ":
        z_count += 1
    elif ch in "yY":
        y_count += 1

print("Number of Z's =", z_count)
print("Number of Y's =", y_count)

#14. check whether a number is prime number or not 
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")




#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
i = 1

while i <= 10:
    print(i)
    i += 1

#print even numbers from 1 to 10
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

#print numbers divisible by both 5 and 7 from 1 to 500 
i = 1

while i <= 500:
    if i % 5 == 0 and i % 7 == 0:
        print(i)
    i += 1


#interview problems
#count digits
n = int(input("Enter a number: "))

count = 0

while n != 0:
    n = n // 10
    count += 1

print("Number of digits =", count)

#reverse a number
n = int(input("Enter a number: "))

reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)

#palindrome number 
n = int(input("Enter a number: "))

original = n
reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")

#palindrome string (without slicing, built in function)
s = input("Enter a string: ")

reverse = ""
i = len(s) - 1

while i >= 0:
    reverse = reverse + s[i]
    i -= 1

if s == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")

#armstrong number
n = int(input("Enter a number: "))

original = n
digits = len(str(n))
sum = 0

while n != 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if original == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
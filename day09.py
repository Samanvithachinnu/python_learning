# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

year = int(input("Enter year: "))
print(is_leap(year))

# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input("Enter number: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
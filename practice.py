#conditional statements
#positive negative zero
n=int(input("enter number:"))
if n>0:
    print(n,"positive")
elif n<0:
    print(n,"negative")
else:
    print(n,"zero")
n=int(int(input("enter n:")))
for i in range(-n,n+1):
    if i>0:
        print(i,"positive")
    elif i<0:
        print(i,"negative")
    else:
        print(i,"zero")
#even odd
n=int(input("enter n:"))
if n%2==0:
    print(n,"even")
else:
    print(n,"odd")
n=int(int(input()))
for i in range(0,n+1):
    if i % 2==0:
        print(i,"even")
    else:
        print(i,"odd")
n=int(input("enter n:"))
if n%5==0:
    print("true")
else:
     print("false")
#largest
n=list(map(int,input("enter values:").split()))
large=n[0]
for i in n:
    if i>large:
        large=i
print(large)
#smallest
n=list(map(int,input("enter values:").split()))
small=n[0]
for i in n:
    if i<small:
        small=i
print(small)
#eligibility to vote
n=int(input("enter age:"))
if n>=18:
    print(n,"eligible to vote")
else:
    print(n,"not eligible to vote")
#pass or fail 
n=int(input("enter marks:"))
if n<=100 and n>=90:
    print(n,"grade A")
elif n<90 and n>=80:
    print(n,"grade B")
elif n<80 and n>=70:
    print(n,"grade c")
elif n<70 and n>=60:
    print(n,"grade d")
else:
    print(n,"Fail")
#leap year  or not 
n=int(input("enter year:"))
if n%4==0 and n%100!=0 or n%400==0:
    print(n,"leap year")
else:
    print(n,"not leap year")
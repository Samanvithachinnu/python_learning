# DO EVERYTHING ON YOUR OWN
n=int(input("enter:"))
for i in range(1,n+1):
    print("*"*i)
for j in range(1,n+1):
    print((n-j)*" "+"*"*j)
n=int(input("enter:"))    
for i in range(1,n+1):
    print((n-i)*" ","* "*i)
n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=int(input("enter:"))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or col==n-row+1 or row==(n+1)//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=int(input("enter:"))
for i in range(n,0,-1):
    if i == n:
        print("*" * (2*n-1))
    else:
        print("*"*i+" "*(2*(n-i)-1),"*"*i)# left * right* and middile space so n=5 i=1,2*(4-1)-1 2*3-1=6-1=5 spaces
n=int(input("enter:"))
for i in range(1,n+1):
    if i == n:
        print("*"*2*(n-1))
    else:
        print("*"*i," "*(2*(n-i)-1),"*"*i)
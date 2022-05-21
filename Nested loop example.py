n=int(input("Enter any number"))
for i in range(1,n+1):
    print()
    for k in range(n-i):
        print(end=" ")
    for j in range(i):
        print(i, end=" ")


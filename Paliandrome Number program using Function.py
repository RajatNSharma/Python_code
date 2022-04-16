n=int(input("Enter the number : "))
def pali(n):
    rev=0
    z=n
    while(z>0):
        rev=rev*10+z%10
        z=z//10
    print(rev)
    if rev==n:
        print("Number is Paliandrome")
    else:
        print("Number is not Paliandrome")
pali(n)


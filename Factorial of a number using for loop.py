n=int(input("Enter any number : "))
if n==0:
    fact=1
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)

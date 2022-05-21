n=int(input("Enter any number : "))
s=0
avg=0
for i in range(1,n+1):
    s=s+i
    avg=s/i
print("Sum of",n, "natural numbers ", s)
print("Avg of",n, "natural numbers ",avg)

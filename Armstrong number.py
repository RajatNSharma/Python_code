n=int(input("Enter the number : "))
orig=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orig==sum:
    print("Number is Armstrong", sum)
else:
    print("Number is not Armstrong", sum)



#Python Program to Find the Sum of the Digits of the Number Recursively
def sum(a):
    if a==0:
        return 0

    else:
         return(a % 10 + sum(a//10))
num=int(input("Enter any number"))
b=sum(num)
print(b)
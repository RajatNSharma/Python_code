#Python Program to Find the Product of two Numbers Using Recursion
def prod(a,b):
    if (a<b):
        return prod(b,a)
    elif (b!=0):
        return (a + prod(a,b-1))
    else:
        return 0
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
result = prod(a,b)
print(result)


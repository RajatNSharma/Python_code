#Python Program to Find the Largest Number in a List
num=[23,29,36,54,66,99,54]
print(max(num))

print("\nAnother method")

l=[]
num=int(input("Enter the number of element : "))
for i in range (1,num+1):
    n=int(input("Enter the element : "))
    l.append(n)
l.sort()
print(l[num-1])






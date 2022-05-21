total_prime=0
total_composite=0

while(1):
    num = int(input("Enter the no. "))
    if(num==-1):
        break
    is_composite=0
    for i in range(2,num):
        if num%i==0:
         is_composite=1
        break
    if(is_composite):
        total_composite+=1
    else:
        total_prime+=1
print("Total composite = ",total_composite)
print("Total Prime = ", total_prime)



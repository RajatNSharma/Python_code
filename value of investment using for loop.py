inval=float(input("enter the amount of investment "))
rt=float(input("Enter the rate of interest "))
yrs=int(input("Enter the years "))
fival=inval
for i in range(1,yrs+1):
    fival=fival*(1+rt/100)
    print(i,"\t\t",fival)
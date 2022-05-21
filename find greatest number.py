num1= int(input("Enter the first number :"))
num2= int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))
if(num1>num2 and num3):
    print(num1, "is greater than", num2, "and", num3 )
elif(num2>num3 and num2):
    print(num2, "is greater than", num1, "and",num3)
elif(num3>num1 and num2):
    print(num3, "is greater than", num1, "and",num2)
else:
    print("All numbers are equal")


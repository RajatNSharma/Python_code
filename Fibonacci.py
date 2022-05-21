a = 0
b = 1
f = 1
n = int(input("Till what number would you like to see the fibonacci sequence: "))
while b <= n:
    f = a+b
    a = b
    b = f
    print(a)


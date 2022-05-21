def report (E,M,S,H,G):
    return ((E+M+S+H+G)/500)*100
E=float(input("Enter the marks of English :"))
M=float(input("Enter the marks of Maths :"))
S=float(input("Enter the marks of Science :"))
H=float(input("Enter the marks of History :"))
G=float(input("Enter the marks of Geography :"))
print(E,M,S,H,G, '\n', report(E,M,S,H,G))


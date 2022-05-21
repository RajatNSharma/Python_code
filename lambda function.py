x=lambda a,b,c: a+b+c
print(x(5,6,2))

print("\nFilter Function Using lambda")

Ages = [5,9,18,21,26]
Adults= filter(lambda a: a>18,Ages)
for x in Adults:
    print(x)

print(len(Ages))








a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
if a>b and a>c:
    d =a
elif c>b and c>a:
    d = c
else:
    d = b
print("Bolshe: ", d)
from math import pi
def ploshad_rectangle(a,b):
    return a*b
def ploshad_square(a):
    return a**2
def plosad_kruga(r):
    return (r**2)*pi

print("Площадь квадрата = ",ploshad_square(5))
print("Площадь прямоугольника = ",ploshad_rectangle(4,5))
print("Площадь круга = ",plosad_kruga(6))

A = []
for i in range(1,100):
    if i%3==0 and i%5==0:
        A.append(i)
print("Следующие значения делятся и на 3, и на 5: ",A)


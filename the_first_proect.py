def perimetr_rectangle(a,b):
    return a+b+a+b
def perimetr_square(a):
    return a*4
def ploshad_rectangle(a,b):
    return a*b
def ploshad_square(a):
    return a**2

print("Площадь квадрата = ",ploshad_square(5))
print("Площадь прямоугольника = ",ploshad_rectangle(4,5))
print("Периметр квадрата = ",perimetr_square(5))
print("Периметр прямоугольника = ",perimetr_rectangle(5,5))


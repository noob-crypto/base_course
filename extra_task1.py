print("ax^2 + bx + c = 0:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = ( b ** 2 - 4 * a * c )
print( d )

if d > 0:
    x1 = (-b + (d)** 0.5) / (2 * a)
    x2 = (-b - (d)** 0.5) / (2 * a)
    print(x1) 
    print(x2) 
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")
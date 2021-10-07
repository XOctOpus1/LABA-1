# circle and line Denys Gordiichuk K28 (Задача №2)
from math import sqrt

class Circle:
    a = 0
    b = 0
    R = 0

class Line:
    k = 0
    b = 0

class Line_2:
    a = 0
    b = 0
    c = 0

class Point:
    x = 0
    y = 0
    def prn(self):
        print(f"x - {self.x}")
        print(f"y - {self.y}")

n = int(input("Привіт, це програма для фігур на площині(Коло і Пряма): '\n' Вибери дію яку хочеш проводити: '\n'1. Перетин фігур '\n'2. Відображення відносно прямої '\n''\n'"))

if n == 1:
    Circle1 = Circle()
    Line1 = Line()


    print("Кола виду (x-a)^2 + (y-b)^2 = R^2")
    Circle1.a = int(input("Enter a for circle'\n'"))
    Circle1.b = int(input("Enter b for circle'\n'"))
    Circle1.R = int(input("Enter R for circle'\n'"))



    print("Пряма виду y = kx + b")
    Line1.k = int(input("Enter k for line'\n'"))
    Line1.b = int(input("Enter b for line'\n'"))


    #       (K^2 + 1)x^2 - 2x(a-ck) + c^2 + R^2 = 0
    #       ax + by + c = 0

    a = Line1.k**2 + 1
    b = 2 * ( (Line1.b - Circle1.b)*Line1.k - Circle1.a )
    c = Circle1.a**2 + (Line1.b - Circle1.b)**2 - Circle1.R**2

    # calculate the discriminant
    d = (b**2) - (4*a*c)

    if d < 0 :
        print("Вони не перетинаються ")
        exit()
    elif d == 0 :
        SOL = Point()
        print("Вони дотикаються в точці ")

        SOL.x = (-b) / (2 * a)
        SOL.y = Line1.k*SOL.x + Line1.b

        SOL.prn()
        exit()
    else:
        SOL1 = Point()
        SOL2 = Point()

        print("Вони перетинаються в точках ")

        SOL1.x = (-b-sqrt(d))/(2*a)
        SOL2.x = (-b+sqrt(d))/(2*a)

        SOL1.y = Line1.k * SOL1.x + Line1.b
        SOL2.y = Line1.k * SOL2.x + Line1.b
        print("Перша точка ")
        SOL1.prn()
        print("Перша точка ")
        SOL2.prn()


elif n == 2:
    Circle1 = Circle()
    Line1 = Line_2()

    print("Кола виду (x-a)^2 + (y-b)^2 = R^2")
    Circle1.a = int(input("Enter a for circle'\n'"))
    Circle1.b = int(input("Enter b for circle'\n'"))
    Circle1.R = int(input("Enter R for circle'\n'"))

    print("Пряма виду Ax + By + C = 0")
    Line1.a = int(input("Enter A for line'\n'"))
    Line1.b = int(input("Enter B for line'\n'"))
    Line1.c = int(input("Enter C for line'\n'"))

    O = Point()
    Per = Point()
    SOL = Point()

    O.x = Circle1.a
    O.y = Circle1.b

    # Перпендикулярна пряма : Bx - Ay + D = 0, де D - константа.

    # Bx0 - Ay0 + D = 0, тобто D = Ay0 - Bx0.
    D = (Line1.a * O.y - Line1.b * O.x)


    # вирішити систему лінійних рівнянь:Ах + By + C = 0,Bx - Ay + Ay0 - Bx0 = 0. Її рішення дасть числа (x1, y1), що служать координатами точки перетину прямих.

    Per.y = ((Line1.a * D - Line1.c*Line1.b) / ((Line1.a)**2 + (Line1.b)**2))
    Per.x = (Line1.a * Per.y - D) / Line1.b

    #х - x1 = x1 - x0, y - y1 = y1 - y0. Отже, x = 2x1 - x0, y = 2y1 - y0.


    SOL.x = 2*Per.x - O.x
    SOL.y = 2 * Per.y - O.y


    print(f"Рівняння колa (x-({Circle1.a}))^2 + (y-({Circle1.b}))^2 = ({Circle1.R})^2 симетрично відображеного від прямої ({Line1.a})x + ({Line1.b})y + ({Line1.c}) = 0 є таке рівняння:  (x-({SOL.x}))^2 + (y-({SOL.y}))^2 = ({Circle1.R})^2")

else:
    exit()




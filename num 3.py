import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        return "Корни не являются вещественными числами"

# Ввод коэффициентов квадратного уравнения с клавиатуры
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисление корней и вывод результата
roots = solve_quadratic_equation(a, b, c)
if isinstance(roots, tuple):
    print("Корни квадратного уравнения:", roots[0], "и", roots[1])
else:
    print(roots)
#задача 1
# def print_lines(n):
#     print("-" * n)
#     print("-" * n)
#
# n = int(input("Введите количество символов: "))
# print_lines(n)

#задача 2
# def print_rectangle(n):
#    if n < 2:
#        print("Ширина должна быть не менее 2-ух")
#    print("-" * n)
#    print("-"+ " " * (n-2)+ "-")
#    print("-" * n)
#
# n = int(input("Введите количество символов: "))
# print_rectangle(n)

#задача 3
# def print_triangle(n):
#     for i in range(1, n + 1):
#         print('*' * i)
# n = int(input("Введите количество символов: "))
# print_triangle(n)

# #задача 4
# def average_of_five(a, b, c, d, e):
#     return (a + b + c + d + e) / 5
#
# print(average_of_five(6, 2, 3, 4, 5))
#
# #задача 5
# def count_digits(number):
#     number = abs(int(number))
#     if number == 0:
#         return 1
#     count = 0
#     while number > 0:
#         count += 1
#         number //= 10
#     return count
# print(count_digits(123456789))
#
# #задача 7
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
#
# def triangle_perimetr(x1,y1,x2,y2,x3,y3):
#     a = distance(x1, y1, x2,y2)
#     b = distance(x2,y2, x3, y3)
#     c = distance(x3,y3,x1,y1)
#     return a+b+c
# print(triangle_perimetr(1, 2, 4, 5, 6, 7))
#
#
# #задача 8
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# primes =[]
# for i in range (100,1000)
#     if is_prime(i):
#         primes.append(i)
# print(primes)
#
# #задача 9
# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return summa
#
#
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счастливое")
#     else:
#         print("Число не счастливое")
# is_lucky(123321)
#
# #задача 10
# def max6(a,b,c,d,e,f):
#     return max(a,b,c,d,e,f)
#
# print(max6(2, 6, 8, 4, 5, 9))
#задача 11
def swap(x, y):
    return y, x

a = 1
b = 2
c = 3
d = 4

print("До обмена:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

a, b = swap(a, b)
c, d = swap(c, d)

print("\nПосле обмена:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

#задача 12
import math

def perimeter(a, b, c):
    return a + b + c

def area(a, b, c):
    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a1, b1, c1 = 8, 9, 10
a2, b2, c2 = 5, 12, 13

sum_perimeters = perimeter(a1, b1, c1) + perimeter(a2, b2, c2)
sum_areas = area(a1, b1, c1) + area(a2, b2, c2)

print(f"Сумма периметров: {sum_perimeters}")
print(f"Сумма площадей: {sum_areas:.2f}")
#
# #задача 13
# def trapezoid_perimetr_area(a, b, h):
#     side = (((a-b)/2)**2 + h**2)**0.5
#     p = a+b+2*side
#     area = (a+b)/2*h
#     return p, area
#
# tr1 = trapezoid_perimetr_area(4, 10, 3)
# tr2 = trapezoid_perimetr_area(5, 10, 7)
# print((f"Сумма периметров трапеций: {tr1[0]+tr2[0]"))
# print((f"Сумма площадей трапеций: {tr1[1]+tr2[1]"))

# #задача 14
# def circle_area(R):
#     return 3,14*R**2
#
# def rectangle_area(a, b):
#     return  a*b
# def triangle_area(a, h):
#     return  (a*h)*0.5
#
# print("1-Круг")
# print("2-Прямоугольник")
# print("3-Треугольник")
# figure = input("Выберете фигуру, площадь которой вы хотите найти: ")
# if figure == "1":
#     R = float(input("Введите радиус круга: "))
#     print(circle_area(R))
# elif figure == "2":
#     a = float(input("Введите сторону а:"))
#     b = float(input("Введите сторону b:"))
#     print(rectangle_area(a, b))
# elif figure == "3":
#     a = float(input("Введите сторону а:"))
#     h = float(input("Введите сторону h:"))
#     print(triangle_area(a, h))
# else:
#     print("Введена ошибочная команда")
#
# #задача 16
# def draw_square(n, s):
#     for _ in range(n):
#         print(n*s)
# side = int(input("Введите сторону квадрата: "))
# symbole = input("Введите символ: ")
# draw_square(side, symbole)
#
# #задача 17
# def deliteli(n):
#     for i in range(1, n+1):
#         if n% i == 0:
#             print(i, end=" ")
#     print()
#
# while True:
#     x = int(input("Введите число (0 до выхода из программы): "))
#     if x == 0:
#         break
#     deliteli(x)
#задача 19
def pointInRect(x, y, x1, y1, x2, y2):
    return (x1 <= x <= x2) and (y2 <= y <= y1)

x, y = 5, 6
x1, y1 = 7, 8
x2, y2 = 7, 2

print(pointInRect(x, y, x1, y1, x2, y2))

#задача 20
def pointInTriangle(x, y, x1, y1, x2, y2, x3, y3):
    def area(a, b, c, d, e, f):
        return abs((a*(d - f) + c*(f - b) + e*(b - d)) / 2)

    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)

    return abs(A - (A1 + A2 + A3)) < 1e-10

x, y = 5, 5
x1, y1 = 3, 7
x2, y2 = 0, 5
x3, y3 = 5, 0

print(pointInTriangle(x, y, x1, y1, x2, y2, x3, y3))

#задача 21
def calculate_score(scores):
    if len(scores) != 5:
        return None
    sorted_scores = sorted(scores)
    return sum(sorted_scores[1:-1]) / 3

scores = [55, 36, 75, 77, 100]
print(calculate_score(scores))


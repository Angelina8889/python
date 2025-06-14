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

#задача 4
def average_of_five(a, b, c, d, e):
    return (a + b + c + d + e) / 5

print(average_of_five(6, 2, 3, 4, 5))

#задача 5
def count_digits(number):
    number = abs(int(number))
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count
print(count_digits(123456789))

#задача 7
def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

def triangle_perimetr(x1,y1,x2,y2,x3,y3):
    a = distance(x1, y1, x2,y2)
    b = distance(x2,y2, x3, y3)
    c = distance(x3,y3,x1,y1)
    return a+b+c
print(triangle_perimetr(1, 2, 4, 5, 6, 7))


#задача 8
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes =[]
for i in range (100,1000)
    if is_prime(i):
        primes.append(i)
print(primes)

#задача 9
def sum_digits(n):
    summa = 0
    for d in str(n):
        summa += int(d)
    return summa


def is_lucky(n):
    s = str(n)
    if sum_digits(s[:3]) == sum_digits(s[3:]):
        print("Число счастливое")
    else:
        print("Число не счастливое")
is_lucky(123321)

#задача 10
def max6(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)

print(max6(2, 6, 8, 4, 5, 9))




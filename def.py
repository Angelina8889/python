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


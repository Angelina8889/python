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
def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
n = int(input("Введите количество символов: "))
print_triangle(n)


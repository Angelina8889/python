#Задача 1
number = (int(input("Введите число от 1 до 7: ")))
if number == 1:
    print('Понедельник')
elif number == 2:
    print('Вторник')
elif number == 3:
    print('Среда')
elif number == 4:
    print('Четверг')
elif number == 5:
    print('Пятница')
elif number == 6:
    print('Суббота')
elif number == 7:
    print('Воскресенье')
else:
    print("Ошибка. Введите число от 1 до 7")

#Задача 2
x = int(input("Введите число: "))
if x % 2 == 0:
    print("Число является четным")
else:
    print("Число не является чётным ")

#Задача 3
y = int(input("Введите число: "))
if y<=9:
    print("Число однозначное")
elif y<=99:
    print("Число двузначное")
elif y<=999:
    print("Число трехзначное")
else:
    print("Число не принадлежит однозначным,двузначным и трехзначным")

#Задача 4
c = int(input("Введите возраст: "))
if c >=18:
    print("Вам можно голосовать")
else:
    print("Вам нельзя голосовать")

#Задача 5
q = float(input("Введите число 1: "))
w = float(input("Введите число 2: "))
e = float(input("Введите число 3: "))
if q >= w and q >= e:
    print(f"Наибольшее число: {q}")
elif w >= q and w >= e:
    print(f"Наибольшее число: {w}")
else:
    print(f"Наибольшее число: {e}")

#Задача 6
s = float(input("Введите число 1: "))
d = float(input("Введите число 2: "))
f = float(input("Введите число 3: "))
if s == d or s == f or d == f:
    print("Среди чисел есть одинаковые")
else:
    print("Все числа различны")

#Задача 7
r = float(input("Введите число 1: "))
t = float(input("Введите число 2: "))
m = float(input("Введите число 3: "))
min_num = min(r, t, m)
max_num = max(r, t, m)
mid_num = (r+ t+ m) - min_num - max_num
print("Числа в порядке возрастания:", min_num, mid_num, max_num)

#Задача 8
p = 200
if p<=500:
    print(p+3)



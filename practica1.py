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
nums = [r,t,m]
nums.sort()
print("Числа в порядке возрастания:", nums[0], nums [1], nums[2])

#Задача 8
sales1 = float(input("Введите уровень продаж для менеджера 1: "))
sales2 = float(input("Введите уровень продаж для менеджера 2: "))
sales3 = float(input("Введите уровень продаж для менеджера 3: "))

if sales1 <= 500:
    salary1 = 200 + sales1 * 0.03
elif sales1 <= 1000:
    salary1 = 200 + sales1 * 0.05
else:
    salary1 = 200 + sales1 * 0.08

if sales2 <= 500:
    salary2 = 200 + sales2 * 0.03
elif sales2 <= 1000:
    salary2= 200 + sales2 * 0.05
else:
    salary2 = 200 + sales2 * 0.08

if sales3 <= 500:
    salary3 = 200 + sales3 * 0.03
elif sales1 <= 1000:
    salary3 = 200 + sales3 * 0.05
else:
    salary3 = 200 + sales3 * 0.08

best_salary = max(salary1, salary2, salary3)
if best_salary == salary1:
    salary1 +=200
    best = 1
elif best_salary == salary2:
    salary2 +=200
    best = 2
else:
    salary3 +=200
    best =3

print(f"Зарплата 1 менеджера: {salary1}")
print(f"Зарплата 1 менеджера: {salary2}")
print(f"Зарплата 1 менеджера: {salary3}")
print(f"Лучший менеджер: {best}-ый")




#Задача 9
year = int(input("Введите год: "))
month = int(input("Введите месяц (1-12): "))
if month == 2:
    if (year % 4 == 0 and year % 100 !=0) or (year %400 == 0):
        print("29 дней")
    else:
        print("28 дней")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 день")
elif month in [4,6,9,11]:
    print("30 дней")
else:
    print("Неккоректный номер месяца")



#задача 10
age = int(input("Введите возраст посетителя: "))
time = int(input("Введите время сеанса (часы, 0-23): "))
price = 0

if age < 3:
    price = 0
elif age <= 12:
    price = 10
else:
    price = 15

if time <= 12 and price > 0:
    price *= 0.8

print(f"Стоимость билета к оплате:{price}")



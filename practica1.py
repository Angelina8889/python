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
def calculate_salary(sales):
    base_salary = 200  # Базовая зарплата
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = sales * 0.05
    else:
        commission = sales * 0.08
    total_salary = base_salary + commission
    return total_salary
sales1 = float(input("Введите уровень продаж для менеджера 1: "))
sales2 = float(input("Введите уровень продаж для менеджера 2: "))
sales3 = float(input("Введите уровень продаж для менеджера 3: "))

salary1 = calculate_salary(sales1)
salary2 = calculate_salary(sales2)
salary3 = calculate_salary(sales3)

max_salary = salary1
best_manager = 1

if salary2 > max_salary:
    max_salary = salary2
    best_manager = 2

if salary3 > max_salary:
    max_salary = salary3
    best_manager = 3

if best_manager == 1:
    salary1 += 200
elif best_manager == 2:
    salary2 += 200
else:
    salary3 += 200

print("\nИтоговые зарплаты менеджеров:")
print(f"Менеджер 1: {salary1} $")
print(f"Менеджер 2: {salary2} $")
print(f"Менеджер 3: {salary3} $")

print(f"\nЛучший менеджер: Менеджер {best_manager} (премия 200$ начислена)")

#Задача 9
def days_in_month(year, month):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

year = int(input("Введите год: "))
month = int(input("Введите месяц (1-12): "))

if month < 1 or month > 12:
    print("Ошибка: месяц должен быть от 1 до 12!")
else:
    days = days_in_month(year, month)
    print(f"В {month}-м месяце {year} года — {days} дней.")

#задача 10
def calculate_ticket_price(age, time):
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    if time <= 12:
        price *= 0.8

    return price



age = int(input("Введите возраст посетителя: "))
time = int(input("Введите время сеанса (часы, 0-23): "))

if age < 0:
    print("Ошибка: возраст не может быть отрицательным!")
elif time < 0 or time > 23:
    print("Ошибка: время должно быть от 0 до 23 часов!")
else:
    cost = calculate_ticket_price(age, time)
    print(f"Стоимость билета: ${cost:.2f}")



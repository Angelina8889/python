# n = 5
# while n < 10:
#     n += 1
#     if n==7:
#         continue
#     print(n)
#
# print("Цикл завершился")


#Задача 8
sales1 = float(input("Введите уровень продаж для менеджера 1: "))
sales2 = float(input("Введите уровень продаж для менеджера 2: "))
sales3 = float(input("Введите уровень продаж для менеджера 3: "))

salaries=[]
for sales in [sales1, sales2, sales3]:
    if sales <= 500:
      percent = 0.03
    elif sales1 <= 1000:
        percent = 0.05
    else:
        percent = 0.08
    salary = 200 + sales * percent
    salaries.append(salary)


best_salary = max(salaries)
best_index  = salaries.index(best_salary)
salaries[best_index] += 200

print(f"Зарплата 1 менеджера: {salaries[0]}")
print(f"Зарплата 1 менеджера: {salaries[1]}")
print(f"Зарплата 1 менеджера: {salaries[2]}")
print(f"Лучший менеджер: {best_index + 1}-ый")


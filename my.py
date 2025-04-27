print("Angelina")

print("вторая строка")

print("Третья срока")

print("Привет","мир","!")

print(55, 67, 78.5, True, False)

a=5
b=10
print(a+b)
print("5+10=", a+b)
print("5+10=", 5+10)

print("4","5","6","7",sep="-")

a = 17
print(a)
a = b = f = 7
print(a,b,f)

a -= 1
a = a - 1
print(a)

print(5/2)
print(5//2)

print(5*2)
print(5**2)

a = 4
b = 10
print("a =",a,"b =",b)
a, b = b, a
print("a =",a,"b =",b)
"""
Третье занятие 
по Python
"""

# ввод значения от пользователя и преобразование в целое число
# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))
# print("a =", a) # вывод переменной а
# print("b =", b) # вывод переменной b
# print("Сумма a+b=", a+b) # вывод суммы двух переменных (а+b)

# целые числа(int)
a = 5
b = 0
c = -10
d = 500000
e = 600_000
print(a, b, c, d, e)

#дробные числа(float)
a = 3.5
b = 0.0
c = -5.6
d = 50_000.000_03
e = 4.5e2
print(a, b, c, d, e)

#логический тип данных (boolean)
# print(bool(0))
# print(bool(-1))
# print(bool(5))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(""))
# print(bool(" "))
# print(bool("Привет мир!"))

print(2 == 2)
print (2 == int("2"))
print (4 < 2)
print (5 >= 5)
print (10 <= 5)
x = 5
a = 1
b = 10
print(a > x < b)

#строки (string)
print("Строка в двойных кавычках")
print('строка в одиночных кавычках')
print("М.Ю Лермонтов 'Бородино'")
print('М.Ю Лермонтов "Бородино"')
print("М.Ю Лермонтов \"Бородино\"")

print("С учётом сложившейся международной обстановки, новая модель \n"
      "организационной деятельности однозначно определяет каждого участника как способного принимать собственные "
      "решения касаемо экономической целесообразности принимаемых решений. Однозначно, диаграммы связей представляют "
      "собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть функционально разнесены на "
      "независимые элементы. В частности, высокотехнологичная концепция общественного уклада способствует подготовке и "
      "реализации системы обучения кадров, соответствующей насущным потребностям. Значимость этих проблем настолько очевидна,"
      " что высокотехнологичная концепция общественного уклада выявляет срочную потребность первоочередных требований. "
      "А также активно развивающиеся страны третьего мира, инициированные исключительно синтетически, "
      "преданы социально-демократической анафеме! Равным образом, высокотехнологичная концепция общественного уклада "
      "создаёт предпосылки для прогресса профессионального сообщества!")
print("Привет" + "мир" + "!") #конкатенация
print ("5"+"5")
print(5+5)
#print(5+"5") #будет ошибка по типу данных
print(5+ int("5"))

print(5 * 3)
print("5" * 3) #дупликация
print("Привет " * 3)

a = 5
b = 10
result = a + b
print(a, "+", b, "=", result)
final = str(a) + " + " + str(b) + " = " + str(result)
print(final)
final_v2 = (f"Результат выражения:\n"
            f" {a} + {b} = {a + b}")
print (final_v2)

#списки(list)
my_list = ["Строка", 567, 78.6, True]
print(my_list)
print(my_list[0])
print(my_list[3])
print(my_list[2:4])
print(my_list[1:])

#кортежи (tupeles)
myTuple = (78, 89.9, True, "Строка")
print(myTuple)
print(myTuple[0])
print(myTuple[3])
print(myTuple[2:4])

#словари(dictionary)
myDict = {"name": "Angelina", "role": "QA", 123: "test-value", 456: 567.67}
print(myDict)
print(myDict["name"])
print(myDict[123])
print(myDict[456])
#print(myDict[0]) будет ошибка так как нет ключа 0
name= "Angelina"
myDict = {
      "name": name,
      "role": "QA"
}
print(myDict["name"])
print(myDict.keys())
print(myDict.values())

#множества (set)
myList = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7]
mySet = set(myList)
print(mySet)

myList = ["Добрый", "добрый", "день", "день"]
mySet = set(myList)
print(mySet)

# преобразование типов данных
а = 5
а = "строка"
а = [5,5,6]

x =5.67
x = int(x)
print(x)
x =str(x)
print(x+"строка")
x = float(x)
print(x)

a = "Привет мир!"
a = list(a)
print(a)

myList = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7]
mySet = set(myList)
myList = list(mySet)
print(myList)

myTuple = tuple(myList)
print(myTuple)

print(ord("а"))
print(chr(1072))
#print(f"\\u {ord("а"):04х}")

#Операторы
a = 5
b = 10
print (a+b)
print (a-b)
print (a*b)
print(a/b)
print(a%b)
print(8%2)
print(a**2)
print(10//3)
print(-10//3)

print(5 == 5)
print(5 != 5)
print(5 > 10)
print(5 < 10)
print(5 >= 10)
print(5 <= 10)

a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a **= b
print(a)
a /= b
print(a)
a //= b
print(a)
a %= b
print(a)




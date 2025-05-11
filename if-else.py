a = 5
b = 5
if a == b:
    print("a равно b")
else:
    print("a НЕ равно b")

print("__________________")

cost=2000
if cost < 1000:
   print("скидки нет")
elif cost < 3000:
    print("скидка 5%")
elif cost < 5000:
    print("скидка 7%")
else:
    print("скидка 10%")

print("-------")
a = int(input("Введите целое число: "))
if a>5:
    print("Это число больше пяти")

print("********")
a = int(input("Введите целое число: "))
if a>0:
   a += 1
else:
    a -= 2
print(a)

print("^^^^^^^^")
x=float(input("Введите число: "))
 if -9 < x < 2:
     print("Число принадлежит интервалу(-9, 2)")
else:
    print("Число не принадлежит интервалу(-9, 2)")



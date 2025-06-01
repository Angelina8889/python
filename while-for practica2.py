# #задача 1
# n = 0
# while n < 50:
#     n +=2
#     print(n)
#
# #задача 2
# sum = 0
# y = 1
# while y <=100:
#     sum += y
#     y += 1
# print("Сумма чисел от 1 до 100:", sum)
#
# #задача 3
# n= int(input("Введите число: "))
# is_prime = True
#
# if n < 2:
#     is_prime = False
# else:
#     for i in range (2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#
# if is_prime == True:
#     print("Число простое")
# else:
#     print("Числе не является простым")
#
# #задача 4
# n= int(input("Введите число: "))
# result = 1
# for i in range(2, n+1):
#     result *= i
#     print(result)
#
# #задача 5
# a, b = 0, 1
# count = 0
# while count < 10:
#     print(a, end=' ')
#     a, b = b, a + b
#     count += 1
#
#
# #задача 6
# for числа in range (10, 0 , -1):
#     print(числа)
#
# #задача 7
# s = input("Введите строку: ")
# vowels = 'аеёиоуыэюяaeiouy'
# count = 0
#
# for char in s.lower():
#     if char in vowels:
#         count += 1
#
# print(f"Количество гласных букв: {count}")
#
# #задача 8
# number = int(input("Введите число: "))
# sum_digits = 0
#
# while number > 0:
#     sum_digits += number % 10
#     number = number // 10
#
# print(f"Сумма цифр: {sum_digits}")
#
# #задача 9
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}", end='\t')
#     print()
#
# #задача 10
# numbers = [0, 15 , -8, 3, -55]
# result = []
# for i in numbers:
#     if abs(i) > 5:
#         result.append(i)
#     print(result)
#
# #задача 11
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# result = ''
# for letter in letters:
#     if not letter.isupper():
#         result += letter
# print(result)
#
# #задача 12
# ww = ["Мавпродош", "Лорнектиф","Древерол", "Фиригарпиг", "Клодобродыч"]
# while True:
#     nickname = input("Введите никнейм: ")
#     if nickname in ww:
#         print(f"Ты – свой. Приветствую, любезный {nickname}!")
#     break
# else:
#     print("Тут ничего нет. Еще есть вопросы?")

#задача 13
alphabet = "аиоуыэеёюябвгджзйклмнпрстфхцчшщъь"
for position in range(11):
   print("^" * 27)
   for letter in alphabet:
       if alphabet.index(letter) % 11 == position:
           print("| ", letter.upper(), letter, " |", end="")
   print()
print("^" *27)

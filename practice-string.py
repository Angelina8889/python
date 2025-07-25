# 1. Напишите программу, которая принимает строку от пользователя и выводит ее в обратном порядке.
# n = input("Введите значение: ")
# print(n[::-1])

#2. Напишите программу, которая принимает две строки и проверяет, являются ли они анаграммами (то есть состоят из одних и тех же символов в любом порядке).
# y = input("Введите значение 1: ").lower()
# x = input("Введите значение 2: ").lower()
# print(sorted(x) == sorted(y))

#3. Напишите программу, которая принимает строку и подсчитывает количество гласных и согласных букв в ней.
# y1 = input("Введите значение: ").upper()
# vowels = "АЕЁИОУЫЭЮЯ"
# consonants = "БВГДЖЗКЛМНПРСТФХЦЧШЩ"
# v = c = 0
# for char in y1:
#     if char in vowels:
#         v += 1
#     elif char in consonants:
#         c += 1
# print("Гласных", v)
# print("Согласных:", c)
#4. Напишите программу, которая принимает строку и проверяет, является ли она палиндромом (то есть одинаково читается в обоих направлениях).
# s = input("Введите значение: ").lower().replace(" ","")
# s2 = s[::-1]
# if s == s2:
#     print("Палиндром")
# else:
#     print("Палиндромом не является")

#*5. Напишите программу, которая принимает строку и выводит на экран все перестановки ее символов.
# s = input("Введите строку: ")
# a = list(s)
# n = len(a)
# index = 0
# stack = [(a, 0)]
#
# while index < len(stack):
#     current, l = stack[index]
#     index += 1
#
#     if l == n - 1:
#         print("".join(current))
#     else:
#         i = n - 1
#         while i >= l:
#             temp = current[:]
#             temp[l], temp[i] = temp[i], temp[l]
#             stack.append((temp, l + 1))
#             i -= 1
#
# #Решение через импорт
# s = input("Введите строку: ")
# perms = permutations(s)
# for p in perms:
#     print("".join(p))
#
#6. Напишите программу, которая принимает строку и удаляет из нее все пробелы
# q = input("Введите строку: ")
# no_spaces = q.replace(" ", "")
# print(no_spaces)

# 7. Напишите программу, которая принимает строку и выводит на экран самое длинное слово в ней
# m = input("Введите строку: ")
# words = m.split()
# longest_word = ""
# for word in words:
#     if len(word)> len(longest_word):
#         longest_word = word
# print("Самое длинное слово: ", longest_word)


#8. Напишите программу, которая принимает строку и заменяет каждое вхождение определенного слова на другое слово.
# m = input("Введите строку: ").lower()
# old = input("Какое слово нужно заменить? ")
# new = input("На какое слово нужно заменить? ")
# print(m.replace(old, new))

#9. Напишите программу, которая принимает строку и проверяет, является ли она панграммой (то есть содержит все буквы алфавита).

# s = input("Введите фразу: ").lower()
# alphabet = ["аиоуыэеюябвгджзйклмнпрстфхцчшщъьё"]
#
# letters_in_s = set()
#  for char in s:
#      if char in alphabet:
#          letters_in_s.add(char)
# if "".join(sorted(letters_in_s)) == alphabet:
#     print("Является панграммой")
# else:
#     print("Не является панграммой")

#10. Напишите программу, которая принимает строку и возвращает новую строку, в которой каждое слово начинается с заглавной буквы.

# s = input("Введите строку: ").lower()
# print(s.title())


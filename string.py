a = [1,2,3,11,12,32,11, -5]
# print(min(a))
# print(max(a))
# print(len(a))
# print(a[len(a)-1])

# print(a.index(12))
# print(a[3])
# print(a.count(11))
#
# string = "Привет мир!"
# print(string.count("!"))

string = "привет мир, Как у Тебя дела? ещё одна фраза. а затем вторая"
print(string.capitalize())
print(string.title())
print(string.upper())
print(string.lower())
print(string.swapcase())
low = string.lower()
print(low.isupper())
print(low.islower())
print(low.istitle())

print(" - " .join(["яблоко", "груша"]))
words = ["Привет", "мир"]
result = " " .join(words)
print(result)

nums = [1, 2, 3]
# print("".join(nums)) будет ошибка по типу данных
print("-".join(map(str, nums)))
print([str(x) for x in nums])

print(string.split(","))

print(string.partition(" "))

print(string.startswith("привет мир"))
print(string.endswith("Вторая"))

print(string.find("привет")) #начинается с 0 индекса
print(string.find("мир")) #начинается с 7-го индекса
print(string.find("и"))
print(string.find("абвгдеж")) #значение не найдено (фиксированный ответ -1)
print(string.find("Привет")) # поиск регистрозависимый (первая буква в оригинале маленькая) т.е. ничего не найдено (-1)

print(string.find("и", 5 )) #поиск с 5-го индекса для буквы и
print(string.find("и", 3, 5))

print(string.replace("мир", "Россия"))
print("привет мир, пока мир".replace("мир", "Россия"))
print("привет Мир, пока мир".replace("мир", "Россия"))
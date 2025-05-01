name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
likes_programming = input("Вам нравится программировать? (да/нет): ")

user_info = {
    "имя": name,
    "возраст": age,
    "любит программировать": likes_programming
}
print("\nИнформация о пользователе:")
print(user_info)
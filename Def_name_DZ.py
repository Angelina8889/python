def greet_and_count(user_name):
    b = user_name.replace(" ","")
    char_count = len (b)
    print(f"Привет, {user_name}. Добро пожаловать!")
    print(f"В твоем имени {char_count} символ(ов)(без пробелов)")

user_name = (input("Введите имя: "))
greet_and_count(user_name)
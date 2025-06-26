# from gc import enable
# from heapq import nsmallest
# from tkinter.font import names
#
#
# class Contact:
#     def __init__(self, name, phone, email):
#         self.name = name
#         self.phone = phone
#         self.email = email
#
#     def __str__(self):
#         return f"{self.name} , Телефон: {self.phone}, Email: {self.email}"
#
# class ContactManager:
#     def __init__(self):
#         self.contacts = []
#
#     def add_contact(self,contact):
#         self.contacts.append(contact)
#         print(f"Контакт '{contact.name}' добавлен")
#
#     def remove_contact(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 self.contacts.remove(contact)
#                 print(f"Контакт '{name}' удален")
#                 return
#         print(f"Контакт с именем '{name}' не найден")
#
#     def find_contact(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 print(f"Контакт найден:")
#                 print(contact)
#                 return
#         print(f"Контакт с именем '{name}' не найден")
#
#     def show_contacts(self):
#         print("\n Ваш список контактов:")
#         for contact in self.contacts
#             print(contact)
#         if not self.contacts:
#             print("Список контактов пуст. Добавьте первого контакта")
#
# def main():
#     manager = ContactManager()
#     while True:
#         print("\n-- Меню --")
#         print("1. Добавить контакт")
#         print("2. Удалить контакт")
#         print("3. Найти контакт")
#         print("4. Показать все контакты")
#         print("5. Выйти из программы")
#
#         choice = input("Выберите пункт меню (1-5): ")
#
#         if choice == "1":
#             name = input("Имя: ")
#             phone = input("Телефон: ")
#             email = input("Email: ")
#             manager.add_contact(Contact(name, phone, email))
#
#         elif choice == "2":
#             name = input("Введите имя для удаления: ")
#             manager.remove_contact(name)
#
#         elif choice == "3":
#             name = input("Введите имя для поиска: ")
#             manager.find_contact(name)
#
#         elif choice == "4":
#             manager.show_contacts()
#
#         elif choice == "5":
#             print("Выход из программы")
#             break
#         else:
#             print("Неверный выбор в меню. Введите число от 1 до 5")
#
# main()
#
# manager = ContactManager()
# contact1 = Contact("Иванов Иван", "123456", "ivanov@test.ru")
# manager.add_contact(contact1)
# contact2 = Contact("Петров", "5556584", "petrov@test.ru")
# manager.add_contact(contact2)
#
# manager.show_contacts()

#dz
#zadacha 1
def F(n):
    if n > 2:
        return  F(n-1) + G(n-2)
    else:
        return n

def G(n):
    if n >2:
        return G(n-1) + F(n-2)
    else:
        return n+1

print(F(4))

#zadacha 2
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))



#zadacha 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rect = Rectangle(8, 12)
print(rect.area())
print(rect.perimeter())

sq = Square(5)
print(sq.area())
print(sq.perimeter())

#zadacha 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, я {self.gender}.")


class Employee(Person):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def work(self):
        print(f"Я работаю как {self.position} и получаю {self.salary} рублей.")

person = Person("Андрей", 28, "мужчина")
person.introduce()

employee = Employee("Алина", 25, "женщина", 85000, "QA инженер")
employee.introduce()
employee.work()
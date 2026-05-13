# Задание

# Во время собеседования вам предложили решить задачу на валидацию имени пользователя.
# Пользователь пытается создать никнейм для своего аккаунта в соцсети Y.
# Правила для корректного никнейма в соцсети Y следующие:

# никнейм должен начинаться с символа @
# никнейм должен содержать от 15 (включительно) символов (включая первый символ @)
# никнейм должен содержать только строчные буквы и (или) цифры (помимо первого символа @)

# Напишите программу, которая выводит «Correct» (без кавычек), если никнейм соответствует
# всем вышеприведённым правилам, или «Incorrect» (без кавычек) в противном случае.

# nickname = input()

# if (nickname.startswith("@") and len(nickname) >= 15 and
#     (nickname[1:].islower() or nickname[1:].isdigit())):
#     print("Correct")
# else:
#     print("Incorrect")


# Int, Float, complex, str, None, bool

# list - список
# dict - словарь
# tuple - кортеж
# set - множество

# lst = [1, 3.4, "HI", True]
# print(lst[1])


# a, b = 5, 7 # Каскадное присваивание
# a = b = c = 3   # Множественное присваивание
# print("Первое число: " +  str(a)) # Конкатенация
# print(str(a) * 5)  # Мультипликация


# a = 5
# b = 6
# print(f"Переменная А = {a}, Переменная B = {b}")
# print("Переменная А = " + str(a) + " Переменная B = " + str(b))
# c = input("Веедите число: ")
# # print(type(c))

# d = "5"
# e = inet(d)
# g = float(e)
# print(type(d), type(e), type(g))
# Инициализация переменной
# название_функции(аргументы функции)


# n1 и n2 (type = int, ввод через клавиатуру )
# print(f"") Сумма: n1 + n2 Разность n1-n2


# s = "hello python"
# print(s[-2:2])
# print(s[2:10:2])
# print(s[::2])
# print(s[::-1])
# print(id(s))
# s[0] = "H"
# print(s)


# n1, n2, n3 = map(int, input().split())

# n1 = int(input())
# n2 = int(input())

# if n1 < n2:
#     print("Первое число меньше второго")
# elif n1 == n2:
#     print("первое число равно второму")
# else:
#     print("Первое число больше второго")

# s = "python"

# lst = [1, 4, 6, 343]

# # for i in s:
# #     print(i)

# for j in range(len(lst)):
#     print(j)


# def имя_функции(параметры):
#     тело функции

# имя_функции(аргументы)

# lst = input().split()
# del lst[0]
# lst[0] = "8"
# lst.remove("-")
# lst.remove("-")
# print("".join(lst))


# Создание словаря
# student = {'имя': "Иван", "возраст": 14, "оценки": [5,4,3,2]}

# # Получение значения по ключу
# print(student["имя"])

# student["любимый_предмет"] = "Русский" # Добавили новый ключ и значение
# student["возраст"] = 16  #Изменили значение существующего ключа

# del student["оценки"]

# print(student)
# # -----------------------------------------

# # Получение значения по ключу,если оно есть в словаре,а иначе
# # дефолтное значение
# print(student.get("яблоко", "Такого ключа у нас нету!!!"))

# # Выводит значение пары (ключ и значение)
# for key, value in student.items():
#     print(f"Ключ: {key}, Значение: {value}")

# # student.clear() -> {}

# print(student.keys())
# print(student.values())
# print(student.pop("имя"))


# names = ["Аня", "Борис", "Влад"]
# scores = [85, 90, 78]

# # Применяем zip
# zipped_data = zip(names, scores)

# # zip создает особый "итератор", чтобы увидеть результат,
# # превратим его в обычный список с помощью list()
# print(list(zipped_data))


# # ----------------------------------------------------------

# # СЛОВАРЬ-ЖУРНАЛ: ключ — имя ученика, значение — список оценок
# journal = {}


# # ---- Функция 1: Добавить ученика ----
# def add_student(name, grades):
#     """Добавляет ученика с его оценками в журнал."""
#     if name in journal:
#         print(f"Ученик '{name}' уже существует в журнале.")
#     else:
#         journal[name] = grades
#         print(f"Ученик '{name}' добавлен.")


# # ---- Функция 2: Средняя оценка одного ученика ----
# def get_average(name):
#     """Возвращает среднюю оценку ученика по его имени."""
#     grades = journal.get(name)  # Используем .get() — безопасно, без ошибок
#     if grades is None:
#         print(f"Ученик '{name}' не найден.")
#         return None
#     average = sum(grades) / len(grades)
#     return round(average, 2)


# # ---- Функция 3: Найти лучшего ученика ----
# def get_best_student():
#     """Находит и возвращает имя ученика с наибольшим средним баллом."""
#     if not journal:  # Если журнал пуст
#         print("Журнал пустой.")
#         return None

#     best_name = None
#     best_avg = 0

#     for name in journal:
#         avg = get_average(name)  # Вызываем уже написанную функцию!
#         if avg > best_avg:
#             best_avg = avg
#             best_name = name

#     return best_name, best_avg


# # ---- Функция 4: Вывести весь журнал ----
# def print_journal():
#     """Красиво выводит весь журнал с средними баллами."""
#     if not journal:
#         print("Журнал пустой.")
#         return

#     print("\n====== ЖУРНАЛ КЛАССА ======")
#     for name, grades in journal.items():  # Используем .items()!
#         avg = get_average(name)
#         print(f"{name:<10} | Оценки: {grades} | Средний балл: {avg}")
#     print("===========================\n")


# # ЗАПУСК ПРОГРАММЫ
# add_student("Аня", [5, 4, 5, 5, 4])
# add_student("Борис", [3, 4, 3, 5, 3])
# add_student("Влад", [4, 4, 5, 4, 5])
# add_student("Аня", [5, 5, 5])  # Попытка добавить дубликат

# print_journal()

# # Средняя оценка конкретного ученика
# print(f"Средний балл Бориса: {get_average('Борис')}")
# print(f"Средний балл Коли:   {get_average('Коля')}")  # Несуществующий ученик

# # Лучший ученик
# best, score = get_best_student()
# print(f"\nЛучший ученик: {best} со средним баллом {score}")

# ---------------------------------------------------------------

# names = ["Аня", "Рома", "Влад"]
# scores = [85, 90, 78, 88]
# years = [2000, 2001, 2002]

# zipped_data = zip(names, scores)

# # print(list(zipped_data))


# print(dict(list(zipped_data)))


# a = {"вавав", 545, 545, 0}
# b = {"вавав", 655, 545, 9}
# print(a)
# # set()
# a.add("dsdsd") # Добавление элемента
# # a.remove("bbb") # вывод ошибки
# a.discard("bbb") # без вывода ошибки
# res = a.difference(a, b)
# print(res)


#---------------------------------------------------

# Шифр Цезаря
# lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
# upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def encrypt(text, step):
#     # Формируем зашифр. текст
#     encrypted_text = ""
#     for char in text:
#         if char.islower():
#             # y = (x + k) mod n - шифрование
#             new_ind = (lower_alphabet.index(char) + step) % 26
#             encrypted_text += lower_alphabet[new_ind]
#         elif char.isupper():
#             new_ind = (upper_alphabet.index(char) + step) % 26
#             encrypted_text += upper_alphabet[new_ind]
#         else:
#             encrypted_text += char

#     return encrypted_text

# def decrypt(text, step):
#     return encrypt(text, -step)

# direction = input("Введите направление (шифрование или дешифрование): ").strip().lower()
# step = int(input("Введите шаг сдвига (целое число): "))
# text = input("Введите текст: ")

# if direction == "шифрование":
#     print("Результат: ", encrypt(text, step))
# elif direction == "дешифрование":
#     print("Результат: ", decrypt(text, step))
# else:
#     print("Ошибка: неверно указано направление!")
#-------------------------------------------

# def encrypt_caesar(plain_text, shift):
#     encrypted_text = ""
#     for char in plain_text:
# # Проверяем, является ли символ буквой
#         if char.isalpha():
#     # Определяем базовый символ (A или a)
#             base = ord('A') if char.isupper() else ord('a')
#     # Сдвигаем символ с учетом базового символа
#             encrypted_char = chr((ord(char) - base + shift) % 26 + base)
#             encrypted_text += encrypted_char
#         else:
#     # Если символ не буква, добавляем его без изменений
#             encrypted_text += char
#     return encrypted_text

# def decrypt_caesar(encrypted_text, shift):
#     return encrypt_caesar(encrypted_text, -shift)

# def main():
#     text = input("Введите текст для шифрования: ")
#     shift = int(input("Введите величину сдвига: "))
#     encrypted = encrypt_caesar(text, shift)
#     print(f"Зашифрованный текст: {encrypted}")
#     decrypted = decrypt_caesar(encrypted, shift)
#     print(f"Расшифрованный текст: {decrypted}")

# if __name__ == "__main__":
#     main()
#---------------------------------------------

# Генератор безопасных паролей

import random

digits_chars = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

num_passwords = int(input("Введите кол-во паролей: "))
len_passwords = int(input("Введите длину одного пароля: "))
digits = input("Включать ли цифры от 0-9 ? ").strip().lower()
upper = input("Включать ли прописные буквы ? ").strip().lower()
lower = input("Включать ли строчные буквы ? ").strip().lower()
punctuation_chars = input("Включать ли !#$%&*+-=?@^_ ? ").strip().lower()
odnaznachniye = input("Включать ли однозначные буквы ? ").strip().lower()

if digits == 'да':
    chars += digits_chars
if upper == 'да':
    chars += uppercase_letters
if lower == 'да':
    chars += lowercase_letters
if punctuation_chars == 'да':
    chars += punctuation

if odnaznachniye == 'да':
    for c in 'il1Lo00':
        chars = chars.replace(c, '')

if len(chars) == 0:
    print('Ошибка: вы не выбрали ни одного символа!')
else:
    for _ in range(num_passwords):
        print(generate_password(len_passwords, chars))
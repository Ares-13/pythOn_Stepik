# a = {0: "А", 1: "В", 2: "Е", 3: "Н", 4: "С"}

# k = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         for g in range(len(a)):
#             for m in range(len(a)):
#                 k += 1
#                 word = a[i] + a[j] + a[g] + a[m]
#                 if "Е" not in word and "АА" not in word:
#                     print(k)  # Выведет 27
#                     exit()

# ------------------------------------------------------------------
# s = "3" * 6 + "4" * 75

# while ("3444" in s) or ("35" in s) or ("355" in s):
#     if "35" in s:
#         s = s.replace("35", "4", 1)
#     else:
#         if "355" in s:
#             s = s.replace("355", "4", 1)
#         else:
#             s = s.replace("3444", "3", 1)

# print(s)  # даст '333333'

# -------------------------------------------------------------------
# with open("Repetitor/13.txt", 'r', encoding='utf-8') as f:
#     seq = list(map(int, f.read().split()))

# not_mult_3 = [x for x in seq if x % 3 != 0 ]
# N = min(not_mult_3)
# print(f"N = {N}")

# pairs = []
# for i in range(len(seq) - 1):
#     a, b = seq[i], seq[i+1]
#     if a % 3 == 0 and b % 3 == 0:
#         pairs.append((a, b))

# print(f"Количество пар: {len(pairs)}")
# if pairs:
#     max_sum = max([a + b for a, b in pairs])
#     print(f"Максимальная сумма: {max_sum}")

# print(*pairs)

# ------------------------------------------------------------

# import pandas as pd

# df = pd.read_excel("Repetitor/7.xls")
# # Первый столбец — дата, остальные — температуры по часам

# df["month"] = pd.to_datetime(df.iloc[:, 0]).dt.month

# # Берём только температурные столбцы (все кроме даты и месяца)
# temp_cols = df.columns[1:-1]
# print(temp_cols)
# # Разворачиваем таблицу: каждая ячейка → отдельная строка
# melted = df.melt(id_vars=["month"], value_vars=temp_cols, value_name="temp")
# print(melted)
# may = melted[(melted["month"] == 5) & (melted["temp"] > 27)]["temp"]
# june = melted[(melted["month"] == 6) & (melted["temp"] > 27)]["temp"]

# diff = june.mean() - may.mean()
# print(int(diff))  # → 3


# import random as r

# Бросок кубика
# print(r.randint(1,6))

# # Случайный выбор
# $colors = ["red", "green", "blue", "red", "green"]
# print(r.choice(colors))

# print(r.random())

# print(r.sample(colors, len(colors)))
# deck = list(range(1, 50))
# print(r.shuffle(deck))
# print(deck[:11])


# from datetime import datetime, date, timedelta

# now = datetime.now()
# print(now)


# birthday = date(2000, 5, 15)
# print(birthday)

# today = date.today()
# print(today)
# res = today + timedelta(weeks=2)
# print(res)


# new_year = date(2027, 1, 1)
# days_left = (new_year - today).days
# print(f"До нового года осталось: {days_left}")


# dt = datetime.strptime("25-12-2026 18:20 Monday-April", "%d-%m-%Y %H:%M %A-%B") # %A
# print(dt.year, dt.month, dt.day)

# now = datetime.now()
# print(now.strftime("%d %B %Y, %A"))

# Вариант 22
# 1. datetime
# Вывести дату через один календарный месяц после заданной.
# Формат даты DD.MM.YYYY
# 2. datetime
# Определить, сколько дней в месяце у введённой даты.
# Формат даты YYYY-MM-DD
# 3. random
# Сгенерировать список из 20 случайных чисел и вывести только те, что
# больше среднего.
# 4. random
# Случайным образом выбрать букву русского алфавита.
# --------------------------------------------------------
# 1. datetime
# date_str = input("Введите дату (DD.MM.YYYY): ")
# d = datetime.strptime(date_str, "%d.%m.%Y").date()

# month = d.month + 1
# year = d.year

# if month > 12:
#     month = 1
#     year += 1

# if month == 12:
#     first_next = date(year+1, 1, 1)
# else:
#     first_next = date(year, month + 1, 1)

# last_day = (first_next - timedelta(days=1)).day

# day = min(d.day, last_day)

# result = date(year, month, day)
# print(result.strftime("%d.%m.%Y"))
# --------------------------------------------------------
# date_str = input("Введите дату (YYYY-MM-DD): ")
# d = datetime.strptime(date_str, "%Y-%m-%d").date()

# if d.month == 12:
#     first_next = date(d.year+1, 1, 1)
# else:
#     first_next = date(d.year, d.month + 1, 1)

# last_day = first_next - timedelta(days=1)
# days_in_month = last_day.day

# print(f"В {d.month}-м месяце {d.year} года: {days_in_month} дней")
# --------------------------------------------------------

# numbers = [r.randint(1,100) for _ in range(20)]
# average = sum(numbers) / len(numbers)

# above_avg = [n for n in numbers if n > average]

# print(f"Список: {numbers}")
# print(f"Среднее: {average}")
# print(f"Больше среднего: {above_avg}")

# --------------------------------------------------------

# russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# random_letter = r.choice(russian_alphabet)

# print(f"Случайная буква: '{random_letter}'")


# import matplotlib.pyplot as plt
# import numpy as np

import turtle
# x = [1, 2, 3, 4, 5, 65, 2, 76, 324, 45]
# y = [25, 45, 52, 65, 78, 32, 12 ,3 ,66, 23]

# plt.plot(x, y, color='green', marker='o', markersize=7)
# plt.xlabel("Ось Х")
# plt.ylabel("Ось Y")
# plt.title("График функции")

# plt.scatter(x, y)

# x = [
#     "Январь",
#     "Февраль",
#     "Март",
#     "Аперль",
#     "Май",
# ]
# y = [120, 250, 100, 50, 600]
# plt.bar(x, y, label="Величина прибыли")
# plt.xlabel("Месяц года")
# plt.ylabel("Прибыль в $")
# plt.legend()

# x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# y = np.tan(x)
# y[:-1][np.diff(y) < 0] = np.nan


# plt.plot(x, y, color='red', linewidth=3)
# plt.ylim(-5, 5)

# plt.xlabel("Ось Х")
# plt.ylabel("Ось Y")
# plt.axhline(0, color='black', linewidth=1)
# plt.axvline(0, color="black", linewidth=1)

# plt.grid(True, linestyle='--', alpha=0.7)

# plt.show()

# vals = [500, 200, 434, 7979]
# cars = ['Ford', 'Lada', 'BMW', 'Mercedes']

# plt.pie(vals, labels=cars, autopct='%1.1f%%')

# plt.show()

#-------------------------------------------------------------------
# def solve(filename):
#     max_dist = 0

#     with open(filename, 'r') as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue

#             # Пропускаем строки с 25 и более буквами A
#             if line.count('A') >= 25:
#                 continue

#             # Для каждой буквы запоминаем первое вхождение
#             first_pos = {}
#             for i, ch in enumerate(line):
#                 if ch not in first_pos:
#                     first_pos[ch] = i   # первый раз встретили — запомнили позицию
#                 else:
#                     # Встретили повторно — считаем расстояние
#                     dist = i - first_pos[ch]
#                     if dist > max_dist:
#                         max_dist = dist

#     return max_dist

# print(solve("Repetitor/inf_26_04_21_24.txt"))
# #---------------------------------------------------------------
# x = 9**8 + 3**5 - 9
# count_2 = 0
# while x > 0:
#     if x % 3 == 2:
#         count_2 += 1
#     x //= 3
# print(count_2)
#-------------------------------------------------------

# with open("Repetitor/17.txt") as f:
#     data = [int(x) for x in f]

# max_3 = max(x for x in data if abs(x) % 10 == 3)
# max_3_sq = max_3**2

# count = 0
# max_sum_sq = -1

# for i in range(len(data) - 1):
#     a, b = data[i], data[i+1]
#     cond1 = (a**2 + b**2) >= max_3_sq
#     cond2 = (abs(a) % 10 == 3) + (abs(b) % 10 == 3) == 1

#     if cond1 and cond2:
#         count += 1
#         max_sum_sq = max(max_sum_sq, a**2 + b**2)

# print(count, max_sum_sq)

#---------------------------------------

# for N in range(1, 1000):
#     bin_N = bin(N)[2:]

#     if N % 2 == 0:
#         r_bin = '10' + bin_N
#     else:
#         r_bin = '1' + bin_N + "00"

#     R = int(r_bin, 2)

#     if R > 107:
#         print(N)
#         break

#---------------------------------------

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((z == w) and (x <= y)) or (not w)
#                 if f == 0:
#                     print(f"{x} {y} {z} {w} | {int(f)}")

#---------------------------------------

# alphabet = ['А', 'Е', 'Л', 'П', 'Р', 'Ь']
# words = []

# for c1 in alphabet:
#     for c2 in alphabet:
#         for c3 in alphabet:
#             for c4 in alphabet:
#                 word = c1 + c2 + c3 + c4
#                 words.append(word)

# for i, w in enumerate(words):
#     if w.count("А") == 1 and w.count("Е") == 1 and "ЕЕ" not in w:
#         print(f'Номер слова: {i+1}')
#         print(f'Само слово: {w}')
#         break

#---------------------------------------

# import ipaddress

# ip = "192.168.108.157"
# mask = "255.255.255.192"

# net = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

# ip_num = int(ipaddress.IPv4Address(ip))
# net_num = int(net.network_address)

# node_number = ip_num - net_num
# print("Номер узла ", node_number)

#---------------------------------------

# p = 5
# q = 7
# e = 11
# f_n = (p-1)*(q-1)

# for d in range(40, 0, -1):
#     if (d*e) % f_n == 1:
#         print(f"Наибольшее значение d: {d}")
#         break

#---------------------------------------

# N = 10 + 510 = 520 символов всего

# N <= 2^i   => i = 10 бит

# 200 * 10 = 2000 бит (объем одного идентификатора)
# 2000 / 8 = 250 байт
# 102400 байт / 250 = 409.6 = 409 пользователей (Ответ)

#---------------------------------------

# number = -72
# bits = 10

# changes = (number & ((1 << bits) - 1))


# 72_10 = 1001000_2 (7 бит)

# 0001001000_2 = 10 бит

# 1110110111_2


#----------------------------------------

# from itertools import permutations, product

# # 1. Описание исходной функции
# def f(x, y, z, w):
#     return (not x or (z and (y <= (w and z))))

# # 2. Находим эталонные строки, при которых F равно 0
# valid_rows = set()
# for x, y, z, w in product([0, 1], repeat=4):
#     if f(x, y, z, w) == 0:
#         valid_rows.add((x, y, z, w))

# # 3. Фрагмент таблицы из условия задачи (None — это пустые ячейки)
# # Каждая строка соответствует строке на картинке
# table_mask = [
#     (1, 1, None, None),
#     (1, None, None, None),
#     (None, 1, None, None),
#     (0, 1, None, 1),
#     (1, None, None, None)
# ]

# # 4. Перебираем перестановку столбцов
# for p in permutations(['x', 'y', 'z', 'w']):
#     # Массив для хранения строк, которые мы сможем восстановить
#     matched_rows = []
    
#     # Пытаемся для каждой строки-маски из условия найти подходящую строчку из эталона
#     for mask in table_mask:
#         for row in valid_rows:
#             # Сопоставляем значения переменных с текущим порядком столбцов p
#             row_dict = {'x': row[0], 'y': row[1], 'z': row[2], 'w': row[3]}
            
#             # Проверяем, совпадает ли эталонная строка с известными цифрами маски
#             is_match = True
#             for col_idx in range(4):
#                 if mask[col_idx] is not None:
#                     var_name = p[col_idx] # Какая переменная стоит в этом столбце
#                     if row_dict[var_name] != mask[col_idx]:
#                         is_match = False
#                         break
            
#             if is_match:
#                 matched_rows.append(row)
#                 break # Нашли подходящую строку для текущей маски, переходим к следующей
                
#     # Если мы смогли успешно подобрать уникальные строки для всех 5 строк маски
#     if len(matched_rows) == 5:
#         # Убедимся, что строки в таблице не повторяются (по условию задачи)
#         if len(set(matched_rows)) >= 4: # Минимум 4 уникальные строки (так как две строки маски (1,?,?,?) идентичны)
#             print("Ответ:", "".join(p))
#             break


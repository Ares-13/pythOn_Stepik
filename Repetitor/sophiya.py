# Задача 1

# n = int(input())
# positions = list(map(int, input().split()))
# positions.sort()

# # Шаг 1: разности между соседними отсортированными колышками
# diffs = [positions[i + 1] - positions[i] for i in range(n - 1)]
# total = sum(diffs)  # сумма всех рёбер = max - min

# # Шаг 2: внутренние рёбра, которые МОЖНО исключить (все кроме первого и последнего)
# excludable = diffs[1 : n - 2]

# # Шаг 3: ДП — максимальная сумма элементов, среди которых нет двух соседних
# if not excludable:
#     max_excl = 0
# elif len(excludable) == 1:
#     max_excl = excludable[0]
# else:
#     m = len(excludable)
#     dp = [0] * m
#     dp[0] = excludable[0]
#     dp[1] = max(excludable[0], excludable[1])
#     for j in range(2, m):
#         dp[j] = max(dp[j - 1], dp[j - 2] + excludable[j])
#     max_excl = dp[-1]

# # Шаг 4: ответ — общая сумма минус максимум исключённого
# print(total - max_excl)

# ----------------------------------------------------------

# Задача 2

# 1 + 2 + 3 + .... p = p * (p+1)/2

# p=5: 1 + 2 + 3 + 4 + 5 = 15  брусков

# добавлено - убрано = k

# p * (p+1)/2 - r = k
# p + r = n

# p * (p+1)/2 - (n - p) = k

# p * (p+1)/2 - n + p = k

# p * (p+1)/2 + p = k + n

# import math

# n,k = map(int, input().split())

# # считаем дискриминант
# D = 9 + 8*(n+k)

# # находим p — количество ходов-установок
# # math.isqrt — целочисленный квадратный корень (без float)
# p = (-3 + math.isqrt(D)) / 2

# # находим r — количество ходов-удалений
# r = n - p
# print(int(r))

# ----------------------------------------------------------


# Задача 3

# Алгоритм Евклида(НОД)
# def gcd(a, b):
#     # а должно быть больше b
#     if a < b:
#         a, b = b, a

#     while b != 0:
#         a, b = b, a % b
#     return a


# # Шаг 1: читаем количество часов
# n = int(input())

# # Шаг 2: читаем периоды всех часов в список
# periods = []
# for i in range(n):
#     t = int(input())
#     periods.append(t)

# # Шаг 3: считаем НОК всех периодов по цепочке
# # НОК(a, b) = a * b // НОД(a, b)

# # Начинаем с первого числа, затем "накатываем" остальные по очереди

# result = periods[0]  # берём первый период как начальное значение

# for i in range(1, len(periods)):
#     a = result
#     b = periods[i]
#     result = a * b // gcd(a,b)

# print(result)


# ----------------------------------------------------------


# Задача 4

# prefix = []
# ?k = prefix[len] - prefix[len-k]
# k = prefix[3] - prefix[1] = 6 - 1 = 5

# +x = db.append(x)   prefix.append(prefix[-1] + x)
# - = db.pop()        prefix.pop()


# Начало: db = [], prefix = [0]

# +1 -> db = [1], prefix = [0, 1]
# +2 -> db = [1,2], prefix = [0, 1, 3]
# +3 -> db = [1,2,3], prefix = [0, 1, 3, 6]
# ?2 -> prefix[-1] - prefix[-1-2] = 6 - 1 = 5 это первый вывод
# - -> убрали 3, db = [1,2], prefix = [0,1,3] , вывод 3
# - -> убрали 2, db = [1], prefix = [0,1] , вывод 2
# ?1 -> prefix[-1] - prefix[-1-1] = 1-0 = 1 это последний вывод

n = int(input("кол-во операций: "))
db = []
prefix = [0]
output = []

for _ in range(n):
    query = input().strip()

    if query[0] == "+":
        # добавлять растение
        x = int(query[1:])
        db.append(x)
        prefix.append(prefix[-1] + x)

    elif query[0] == "-":
        # удаляем последнее растение
        removed = db.pop()
        prefix.pop()
        output.append(removed)

    elif query[0] == "?":
        # сумма последних k растений
        k = int(query[1:])
        total = prefix[-1] - prefix[-1 - k]
        output.append(total)

print("\nВывод результатов:")
print("\n".join(map(str, output)))

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


# s = "3" * 6 + "4" * 75

# while ("35" in s) or ("355" in s) or ("3444" in s):
#     if "35" in s:
#         s = s.replace("35", "4", 1)
#     elif "355" in s:
#         s = s.replace("355", "4", 1)
#     else:
#         s = s.replace("3444", "3", 1)

# print(s)  # даст '333333'


with open("Repetitor/13.txt", 'r', encoding='utf-8') as f:
    seq = list(map(int, f.readline().split()))

not_mult_15 = [x for x in seq if x % 15 != 0 ]
N = min(not_mult_15)
print(f"N = {N}")

pairs = []
for i in range(len(seq) - 1):
    a, b = seq[i], seq[i+1]
    if a % 15 == 0 and b % 15 == 0:
        pairs.append((a, b))

print(f"Количество пар: {len(pairs)}")
if pairs:
    max_sum = max([a + b for a, b in pairs])
    print(f"Максимальная сумма: {max_sum}")

#print(*pairs)

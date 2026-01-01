# s = input().split()
# fl = list(map(float, s))
# for f in fl[:3]:
#     print(f, end=' ')
# print(*fl)

# lst = list(map(lambda n: abs(int(n)), input().split()))
# print(*lst)


# import sys
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst2D = [list(map(int, row.strip())) for row in lst_in]

# s = input().split()
# tp = tuple(map(tuple, [i.split('=') for i in s]))
# print(tp)


s = input().lower()
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
new_s = ''
# 1) разбить предложение на слова
# 2) перебрать каждое слово по буквам и сделать замену из t
# 3) соединить преобразования с помощью join

for i in s: 
    if i in t.keys():
        new_s += t[i] 
    else:
        new_s += '-'
print(new_s)

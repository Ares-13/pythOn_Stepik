# lst = [1, 54, 324, -3, 0, 324]
# lst2 = [45, 65, True]
# lst.append((100, 250))
# lst.insert(1, 52)
# lst.clear()
# lst.remove(1)
# n = lst.pop()
# lst.copy()
# ind = lst.index(324)
# lst.reverse()
# lst[::-1]
# n = lst.count(324)
# lst.sort()


# age = 18
# status = "взрослый" if age >= 18 else "ребенок"
# print(status)

# score = 85
# result = "Отлично" if score >= 90 else "Хорошо" if score >= 80 else "Удовл."


# while <условие>:
#     тело цикла...


# Предусловие
# x = 0
# while x < 5:
#     print(x)
#     x+=1

# Постусловие whike True: ...
# s = 0
# d = 1
# while d !=0:
#     d = int(input("Введите целое число: "))
#     if d % 2 == 0:
#         continue
#     s += d
#     print("s = " + str(s))

# x = int(input())
# if (x > 5 and x < 10) and (x % 2 == 0):
#     print(x)
# else:
#     print("Число в не диапозоне чисел")

#--------------------------------------------


# for <локальная переменная> in <итерируемый обьект>:
#     тело цикла.....

# lst = [1, 54, 324, -3, 0, 324]

# # for i in lst:
# #     print(i)

# s = "hihihih"
# for i in range(len(s)):
#     print(i)

#--------------------------------------------

digs = [4, 3, 100, -53, -30, 1, 34, -8]

# for i in range(len(digs)):
#     if 10 <= abs(digs[i]) <= 99:
#         digs[i] = 0

   
for i, d in enumerate(digs):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0
print(digs)  
# # def trace(func):
# #     def wrapper(*args, **kwargs):
# #         print(f"\nTRACE: calling {func.__name__}() with {args} and {kwargs}\n")

# #         original_func = func(*args, **kwargs) # func() это say()

# #         # !r используется для отладки — чтобы явно видеть тип данных(!s default)
# #         print(f"TRACE: calling {func.__name__}() returned {original_func!r}\n")

# #         return original_func  # без return теряется результат и будет None

# #     return wrapper


# # @trace
# # def say(name, line):
# #     return f'{name}: {line}'


# # say("Jane", "Hello, World")


# def func_show(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f"Площадь прямоугольника: {res}")
#         return res
#     return wrapper


# @func_show
# def get_sq(width, height):
#     return width * height


# res = get_sq(3, 5)


# def make_dict(func):
#     def wrapper(str1, str2):
#         lst1, lst2 = func(str1, str2)
#         d = {lst1[i]: lst2[i] for i in range(len(lst1))}
#         return d

#     return wrapper


# s1 = input()
# s2 = input()


# @make_dict
# def get_list(s1, s2):
#     return s1.split(), s2.split()


# d = get_list(s1, s2)
# print(*sorted(d.items()))


t = {
    "ё": "yo",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


# Декоратор с параметром
def replace_chars(chars=" !?"):
    def decorator(func):
        def wrapper(string):
            # Сначала вызываем исходную функцию (транслитерацию)
            result = func(string)

            # Заменяем указанные символы на дефис
            for char in chars:
                result = result.replace(char, "-")

            # Убираем повторяющиеся дефисы
            while "--" in result:
                result = result.replace("--", "-")

            return result

        return wrapper

    return decorator


# Функция транслитерации
@replace_chars(chars="?!:;,. ")
def transliterate(string):
    low_str = string.lower()
    new_str = "".join([t.get(i, i) for i in low_str])
    return new_str


# Ввод и вывод
s = input()
res = transliterate(s)
print(res)

# Переменная - ячейка памяти,куда сохраняем мы значения(ссылка на обьект в памяти)

#a = 5   # Int
A = 10.5 # Float
name = "Демид" # Str

bool_a = True # Boolean

#print(bool_a, a, name, A)

# = присвание
# == равенство -> True/False


a = 150
b = 54 # каскадное присваивание 
с, d = 100, 500 # Множественное присваивание 

print(a, b)


a, b = b, a # операция обмена значениями
print(a, b)

print(type(a), type(name)) # type() чтобы узнать тип данных



number1 = 3
number2 = 10


# Основные арифметические операции
print(number1 + number2) # сложение
print(number2 - number1) # вычитание
print(number1 * number2) # умножение
print(number2 / number1) # деление
print(number2 // number1) # деление(целое число)
print(number2 % number1) # остаток деления
print(number1**3) # возведение в степень


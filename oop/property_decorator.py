# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.__age = age

#     @age.deleter
#     def age(self):
#         del self.__age
#     # property вызывает эти методы и автоматом выбирает что делать
#     #old = property(get_old, set_old)

# p = Person('John', 35)
# del p.age
# #p.age = 25
# print(p.__dict__)


from string import ascii_letters

class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) == 0:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            # список разрешенных символов
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО разрешаются только буквы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int and 14 > old or old > 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне от 14 до 120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть больше 20кг")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit:
                raise TypeError("Должны быть только цифры")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps
    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person("Никита Сабиров Рустамович", 20, "1237 777719", 57.6)
p.weight = 25.0
print(p.weight)
from accessify import private, protected

class Point:
    # Атрибуты
    circle = 2
    color = 'red'

    # def __new__(cls, *args, **kwargs): #cls обращается к классу,а self к экземпляру класса
    #     print("вызов __new__ " + str(cls))
    #     return super().__new__(cls)

    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y): 
            self.__x = x
            self.__y = y 

    #@private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # def __del__(self):
    #    print("удаление экземпляра " + str(self))

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('error 404')

    def get_coords(self):
        return (self.__x, self.__y)

pt = Point(1, 2)
pt.set_coords(10, 21)
print(pt.get_coords())

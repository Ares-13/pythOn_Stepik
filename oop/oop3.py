class Point:
    # Атрибуты
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("error 404")

    def get_coords(self):
        return (self.__x, self.__y)


pt = Point(1, 2)
pt.set_coords(10, 21)
print(pt.get_coords())

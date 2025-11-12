class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    # def __del__(self):
    #    print("удаление экземпляра " + str(self))

    # def set_coords(self, x, y):
    #     self.x = x
    #     self.y = y

    def get_coords(self):
        return (self.x, self.y)

    @staticmethod
    def norm2(x, y):
        return x**2 + y**2

v = Vector(1, 20)
res = v.get_coords()
print(res)
print(Vector.norm2(2, 5))
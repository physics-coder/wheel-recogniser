import math


class Point:
    def __init__(self, x_coor, y_coor=None, polar=False):
        if type(x_coor) == Point:
            self.x = x_coor.x
            self.y = x_coor.y
        else:
            if not polar:
                self.x = x_coor
                self.y = y_coor
            else:
                self.y = math.sin(y_coor) * x_coor
                self.x = math.cos(y_coor) * x_coor

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def dist(self, x_coor=None, y_coor=None):
        if not x_coor and not y_coor:
            return self.__abs__()
        elif x_coor and not y_coor:
            return math.hypot((self.x - x_coor.x), (self.y - x_coor.y))
        else:
            return math.hypot((self.x - x_coor), (self.y - y_coor))


class Vector(Point):
    def __init__(self, a, b=None, a1=None, b1=None):
        super().__init__(a1 - a, b1 - b)

    def __xor__(self, v):
        return self.x * v.y - self.y * v.x

    def cross_product(self, v):
        return self.__xor__(v)

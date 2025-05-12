from vec2 import Vec2


class Grid:
    def __init__(self, dim: Vec2, value = None):
        self.__dim = dim
        self.__values = [value] * (dim.x * dim.y)

    @property
    def dim(self):
        return self.__dim

    @property
    def width(self):
        return self.__dim.x

    @property
    def height(self):
        return self.__dim.y

    def index_to_pos(self, index):
        quot, rem = divmod(index, self.__dim.x)
        return Vec2(rem, quot)

    def pos_to_index(self, pos: Vec2):
        return pos.y * self.__dim.x + pos.x

    def contains(self, pos: Vec2):
        return pos.x < self.__dim.x and pos.y < self.__dim.y

    def __getitem__(self, pos):
        return self.__values[self.pos_to_index(pos)]

    def __setitem__(self, pos, value):
        self.__values[self.pos_to_index(pos)] = value

    def __str__(self):
        res = ""
        for j in range(self.__dim.y):
            for i in range(self.__dim.x):
                res += f"{self[Vec2(i, j)]}"
            if j < (self.__dim.y - 1):
                res += "\n"
        return res

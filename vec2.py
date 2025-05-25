class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vec2(self.x * value, self.y * value)

    def __truediv__(self, value):
        return Vec2(self.x / value, self.y / value)

    def __floordiv__(self, value):
        return Vec2(self.x // value, self.y // value)

    def __mod__(self, value):
        return Vec2(self.x % value, self.y % value)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, value):
        self.x *= value
        self.y *= value
        return self

    def __idiv__(self, value):
        self.x /= value
        self.y /= value
        return self

    def __ifloordiv__(self, value):
        self.x //= value
        self.y //= value
        return self

    def __imod__(self, value):
        self.x %= value
        self.y %= value
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f"({self.x};{self.y})"

    def __repr__(self):
        return f"({self.x};{self.y})"

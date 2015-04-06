class Hex:
    directions = [
       (+1,  0), (+1, -1), ( 0, -1),
       (-1,  0), (-1, +1), ( 0, +1)
    ]

    def __init__(self, q, r, name=None):
        self.q = q
        self.r = r

        self.name = name

    def __repr__(self):
        return 'Hex({}, {})'.format(self.q, self.r)

    def __str__(self):
        return str(self.name) if self.name is not None else ''

    def __add__(self, other):
        return Hex(self.q+other.q, self.r+other.r)

    def to_cube(self):
        x = self.q
        z = self.r
        y = -x-z
        return Cube(x, y, z, self.name)

    def neighbor(self, direction):
        return self + Hex(*self.directions[direction])


class Cube:
    def __init__(self, x, y, z, name=None):
        self.x = x
        self.y = y
        self.z = z

        self.name = name

    def __repr__(self):
        return 'Cube({}, {}, {})'.format(self.x, self.y, self.z)

    def __str__(self):
        return str(self.name) if self.name is not None else ''

    def __add__(self, other):
        return Cube(self.x+other.x, self.y+other.y, self.z+other.z)

    def to_hex(self):
        q = self.x
        r = self.z
        return Hex(q, r)

    def to_cart(self):
        q = self.x
        r = int(self.z + (self.x + (self.x&1)) / 2)

        x = q
        y = (not (q&1)) + (2 * r)
        return Cart(x, y, self.name)


class Cart:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y

        self.name = name

    def __repr__(self):
        return 'Cart({}, {})'.format(self.x, self.y)

    def __str__(self):
        return str(self.name) if self.name is not None else ''

    def __add__(self, other):
        return Cart(self.x+other.x, self.y+other.y)

from common import *


KEY_MAP = {
    'w': (2, -1),
    's': (2, +1),
    'a': (0, -1),
    'd': (0, +1),
}


def get_dir(inp):
    inp = inp.lower()
    d = [0, 0, 0]

    for key in inp:
        if key in KEY_MAP:
            a = KEY_MAP[key]
            d[a[0]] += a[1]

    return Cube(*d)

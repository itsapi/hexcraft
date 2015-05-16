from common import *


KEY_MAP = {
    'd': [(0, +1)],
    'q': [(0, -1)],
    'e': [(0, +1), (2, -1)],
    'a': [(0, -1), (2, +1)],
    'w': [(2, -1)],
    's': [(2, +1)]
}


def get_dir(inp):
    inp = inp.lower()
    d = [0, 0, 0]

    for key in inp:
        if key in KEY_MAP:
            a = KEY_MAP[key]
            for axis in a:
                d[axis[0]] += axis[1]

    return Cube(*d)

import sys
from time import time

from nbinput import *
from common import *
import game as g


class NamedHex(Hex):
    def __init__(self, q, r, name=''):
        super().__init__(q, r)
        self._name = name

    @property
    def name(self):
        return '{:2}'.format(self._name[:2])

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return self.name


def print_hex(cells, player):

    cart_cells = [cell.to_cart() for cell in cells]
    player = player.to_cart()

    min_x = min(cart_cells, key=lambda c: c.x).x
    min_y = min(cart_cells, key=lambda c: c.y).y
    max_x = max(cart_cells, key=lambda c: c.x).x
    max_y = max(cart_cells, key=lambda c: c.y).y

    x_len = 3 * (1+max_x-min_x)
    y_len = 3 + max_y-min_y

    out = [[' ' for x in range(x_len)] for y in range(y_len)]

    for c_cell, cell in zip(cart_cells, cells):

        x = (c_cell.x - min_x) * 3
        y = c_cell.y - min_y

        out[y  ][x+1:x+3] =   '__'
        out[y+1][x  :x+4] =  '/{}\\'.format('##' if player == c_cell else cell)
        out[y+2][x  :x+4] = '\\__/'

    print('\n'.join(''.join(row) for row in out))


def gen_board(radius):
    return [
        NamedHex(q, r)
            for q in range(-radius, 1+radius)
            for r in range(-radius, 1+radius)
            if abs(q+r) <= radius
    ]


def main():
    FPS = 40
    IPS = 10
    last_frame = 0
    last_input = 0
    change = True

    board = gen_board(5 if len(sys.argv) < 2 else int(sys.argv[1]))
    player = Cube(0, 0, 0)

    with NonBlockingInput() as nbi:
        while True:

            c = escape_code(nbi)
            if c and time() > last_input + 1/IPS:
                c = c.lower()
                if c == chr(27):
                    sys.exit('Quitting')

                d = g.get_dir(c)
                player += d
                if d != Cube(0,0,0):
                    change = True

            if change and time() > last_frame + 1/FPS:
                last_frame = time()
                change = False
                print_hex(board, player)


if __name__ == '__main__':
  main()

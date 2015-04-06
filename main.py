from common import *


def hex_rows(cells):

    cart_cells = [cell.to_cart() for cell in cells]

    min_x = min(cart_cells, key=lambda c: c.x).x
    min_y = min(cart_cells, key=lambda c: c.y).y
    max_x = max(cart_cells, key=lambda c: c.x).x
    max_y = max(cart_cells, key=lambda c: c.y).y

    x_len = 3 * (1+max_x-min_x)
    y_len = 3 + max_y-min_y

    out = [[' ' for x in range(x_len)] for y in range(y_len)]

    for cell in cart_cells:

        x = (cell.x - min_x) * 3
        y = cell.y - min_y

        out[y  ][x+1:x+3] =   '__'
        out[y+1][x  :x+4] =  '/  \\'
        out[y+2][x  :x+4] = '\\__/'

    print('\n'.join(''.join(row) for row in out))


def gen_board(radius):
    return [
        Hex(q, r)
            for q in range(-radius, 1+radius)
            for r in range(-radius, 1+radius)
            if abs(q+r) <= radius
    ]


def main():
    hex_rows(gen_board(9))


if __name__ == '__main__':
  main()

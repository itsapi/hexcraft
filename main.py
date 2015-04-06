def hex_rows(cells):
    x_len = 4 + (6 * (max(cells, key=lambda c: c[0])[0]))
    y_len = 3 + max(cells, key=lambda c: c[1])[1]

    out = [[' ' for x in range(x_len)] for y in range(y_len)]

    for cell in cells:
        if len(cell) == 3:
            cx, cy, c = cell
        else:
            cx, cy = cell
            c = ''

        x = cx*6
        y = cy

        if cy % 2 == 1:
            x += 3

        out[y]  [x+1:x+3] =  '__'
        out[y+1][x:x+4] =   '/{:2}\\'.format(c)
        out[y+2][x:x+4] =  '\\__/'

    print('\n'.join(''.join(row) for row in out))


def main():
    hex_rows(
        [(y//2+x,10-y) for y in range(10) for x in range(10-y)]+
        [(x,y+12,y) for y in range(0,15,2) for x in range(10)]+
        [(x,y+11) for y in range(2,15,2) for x in range(9)]+
        [(y//2+x,y+28) for y in range(10) for x in range(10-y)]
    )


if __name__ == '__main__':
  main()

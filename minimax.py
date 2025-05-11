from math import inf as infv
from random import choice
import platform
import time
from os import system

P1 = -1
P2 = +1
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def score_eval(b):
    if check_win(b, P2):
        val = +1
    elif check_win(b, P1):
        val = -1
    else:
        val = 0
    return val

def check_win(b, p):
    c = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[2][0], b[1][1], b[0][2]],
    ]
    return [p, p, p] in c

def is_done(b):
    return check_win(b, P1) or check_win(b, P2)

def open_spots(b):
    s = []
    for i, r in enumerate(b):
        for j, e in enumerate(r):
            if e == 0:
                s.append([i, j])
    return s

def is_valid(i, j):
    return [i, j] in open_spots(grid)

def mark(i, j, p):
    if is_valid(i, j):
        grid[i][j] = p
        return True
    return False

def ai_move(b, d, p):
    if p == P2:
        opt = [-1, -1, -infv]
    else:
        opt = [-1, -1, +infv]

    if d == 0 or is_done(b):
        sc = score_eval(b)
        return [-1, -1, sc]

    for m in open_spots(b):
        i, j = m[0], m[1]
        b[i][j] = p
        s = ai_move(b, d - 1, -p)
        b[i][j] = 0
        s[0], s[1] = i, j

        if p == P2:
            if s[2] > opt[2]:
                opt = s
        else:
            if s[2] < opt[2]:
                opt = s

    return opt

def reset():
    osys = platform.system().lower()
    if 'windows' in osys:
        system('cls')
    else:
        system('clear')

def show(b, m1, m2):
    sym = {-1: m2, +1: m1, 0: ' '}
    ln = '---------------'
    print('\n' + ln)
    for r in b:
        for e in r:
            ch = sym[e]
            print(f'| {ch} |', end='')
        print('\n' + ln)

def bot_turn(m1, m2):
    d = len(open_spots(grid))
    if d == 0 or is_done(grid):
        return
    reset()
    print(f'Computer turn [{m1}]')
    show(grid, m1, m2)

    if d == 9:
        i = choice([0, 1, 2])
        j = choice([0, 1, 2])
    else:
        m = ai_move(grid, d, P2)
        i, j = m[0], m[1]

    mark(i, j, P2)
    time.sleep(1)

def player_turn(m1, m2):
    d = len(open_spots(grid))
    if d == 0 or is_done(grid):
        return

    mv = -1
    mvs = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    reset()
    print(f'Human turn [{m2}]')
    show(grid, m1, m2)

    while mv < 1 or mv > 9:
        try:
            mv = int(input('Use numpad (1..9): '))
            c = mvs[mv]
            ok = mark(c[0], c[1], P1)
            if not ok:
                print('Invalid')
                mv = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Wrong')

def start():
    reset()
    p2 = ''
    p1 = ''
    f = ''

    while p1 != 'O' and p1 != 'X':
        try:
            print('')
            p1 = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Wrong')

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    reset()
    while f != 'Y' and f != 'N':
        try:
            f = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Wrong')

    while len(open_spots(grid)) > 0 and not is_done(grid):
        if f == 'N':
            bot_turn(p2, p1)
            f = ''

        player_turn(p2, p1)
        bot_turn(p2, p1)

    if check_win(grid, P1):
        reset()
        print(f'Human turn [{p1}]')
        show(grid, p2, p1)
        print('YOU WIN!')
    elif check_win(grid, P2):
        reset()
        print(f'Computer turn [{p2}]')
        show(grid, p2, p1)
        print('YOU LOSE!')
    else:
        reset()
        show(grid, p2, p1)
        print('DRAW!')

    exit()

if __name__ == '__main__':
    start()

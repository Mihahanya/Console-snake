from time import time
from keyboard import is_pressed, wait
from random import randint
import os, sys

w = h = 15
margin = 2

score = 0
move = [1, 0]
parts_of_snake = [[3+i, 3] for i in range(3)]
apple_pos = [randint(0, w-1), randint(4, h-1)]

os.system(f'mode con cols={w*2+margin*4} lines={h+margin*2}')
timer = time()

while True:
    move = [-1, 0] if is_pressed('a') else [1, 0] if is_pressed('d') else [0, -1] if is_pressed('w') else [0, 1] if is_pressed('s') else move

    if time() >= timer:
        if apple_pos in parts_of_snake:
            score += 1
            while 'r' not in locals() or r in parts_of_snake: r = [randint(0, w-1), randint(0, h-1)]
            apple_pos = r
        else: parts_of_snake = parts_of_snake[1:]

        if len([t for t in parts_of_snake if parts_of_snake.count(t) == 1]) != len(parts_of_snake) or parts_of_snake[-1][0] < 0 or parts_of_snake[-1][0] >= w or parts_of_snake[-1][1] < 0 or parts_of_snake[-1][1] >= h:
            sys.stdout.write(f'\nYOU LOSE!!!\nYOUR SCORE IS {score}\npress ENTER to continue...')

            wait('enter')
            os.system('cls')

            score = 0
            move = [1, 0]
            parts_of_snake = [[3 + i, 3] for i in range(3)]

        parts_of_snake.append([parts_of_snake[-1][0] + move[0], parts_of_snake[-1][1] + move[1]])

        result = f'SCORE: {score}' + '\n' * margin + ' '*margin*2
        for y in range(h):
            for x in range(w):
                if [x, y] in parts_of_snake: result += '█'*2
                elif [x, y] == apple_pos: result += '()'
                else: result += '+ '
            result += '\n' * (1 if y != h - 1 else margin) + ' '*margin*2*(y != h-1)

        sys.stdout.write(result)
        timer = time() + 0.3

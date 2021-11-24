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

def out_of_edges(point: list[2]) -> bool:
    return point[0] < 0 or point[0] >= w or point[1] < 0 or point[1] >= h

def is_unique(mass: list) -> bool:
    for t in mass:
        if mass.count(t) > 1:
            return False
    return True

while True:
    move = [-1, 0] if is_pressed('a') else [1, 0] if is_pressed('d') else \
           [0, -1] if is_pressed('w') else [0, 1] if is_pressed('s') else move

    if time() >= timer:
        # Check the snake is alive
        if not is_unique(parts_of_snake) or out_of_edges(parts_of_snake[-1]):
            sys.stdout.write(f'\nYOU LOSE!!!\nYOUR SCORE IS {score}\npress ENTER to continue...')
            score, move, parts_of_snake = 0, [1, 0], [[3 + i, 3] for i in range(3)]

            wait('enter'), os.system('cls')

        # Check the collision with the apple
        if apple_pos in parts_of_snake:
            score += 1
            while 'r' not in locals() or r in parts_of_snake: r = [randint(0, w-1), randint(0, h-1)]
            apple_pos = r
        else: parts_of_snake = parts_of_snake[1:]

        # Move snake
        last = parts_of_snake[-1]
        parts_of_snake.append([last[0] + move[0], last[1] + move[1]])

        # Render a picture
        result = f'SCORE: {score}' + '\n' * margin
        for y in range(h):
            result += ' ' * margin * 2
            for x in range(w):
                if [x, y] in parts_of_snake: result += '█'*2
                elif [x, y] == apple_pos: result += '()'
                else: result += '+ '
            result += '\n' * (1 if y != h - 1 else margin)

        sys.stdout.write(result)
        timer = time() + 0.25

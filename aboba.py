"""
if is_pressed('a'):
    move = [-1, 0]
elif is_pressed('d'):
    move = [1, 0]
elif is_pressed('s'):
    move = [0, 1]
elif is_pressed('w'):
    move = [0, -1]


last = parts_of_snake[-1]
new_part = [last[0] + move[0], last[1] + move[1]]
parts_of_snake.append(new_part)


r = [randint(0, w - 1), randint(0, h - 1)]
while r in parts_of_snake:
    r = [randint(0, w - 1), randint(0, h - 1)]
apple_pos = r


if y != h - 1:
    result += '\n'
else:
    result += '\n' * margin


result = f'SCORE: {score}' + '\n' * margin
for y in range(h):
    result += ' '*margin*2
    for x in range(w):
        if [x, y] in parts_of_snake:
            result += '█'*2
        elif [x, y] == apple_pos:
            result += '()'
        else:
            result += '+ '
    result += '\n' * (1 if y != h - 1 else margin)
"""

print([1, -1])

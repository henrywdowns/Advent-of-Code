from core import AOCD

puzzle = AOCD(1,2025)
data = puzzle.data

data = data.split('\n')

base = 50
zero_count = 0

def turn(current_pos,value):
    dir = value[0].upper()
    if dir not in ['L','R']:
        raise ValueError
    num = int(value[1:])
    if dir == 'L':
        return current_pos - num
    else:
        return current_pos + num

for x in data:
    base = turn(base,x)
    if base%100 == 0:
        zero_count += 1

print(zero_count)

puzzle.submit_answer(zero_count)